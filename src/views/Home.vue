<template>
  <div>
    <!-- Navigation -->
    <nav class="nav">
      <!-- Logo -->
      <div class="logo">Harvest</div>
      <!-- Navigation Links -->
      <div class="nav-links">
        <router-link to="/" class="nav-link">
          <i class="fas fa-home"></i> Home
        </router-link>
        <router-link to="/profile" class="nav-link">
          <i class="fas fa-user"></i> Profile
        </router-link>
        <router-link to="/jobs" class="nav-link">
          <i class="fas fa-briefcase"></i> Jobs
        </router-link>
        <router-link to="/login" class="btn btn-login">
          <i class="fas fa-sign-in-alt"></i> Login
        </router-link>
        <router-link to="/signup" class="btn btn-signup">
          <i class="fas fa-user-plus"></i> Signup
        </router-link>
      </div>
    </nav>
    
    <!-- Home Page Content -->
    <div class="home-page">
      <!-- Hero Section -->
      <Hero @search="handleSearch" />
      <!-- Main Content Sections -->
      <div class="main-content">
        <!-- Job Listings -->
        <section class="job-listings">
          <h2>Job Listings</h2>
          <JobList :jobs="filteredJobs" @selectJob="selectJob" @jobSaved="handleJobSaved" />
        </section>


        <section class="empty-section">
          <h2>Job Statuses</h2>
          <div class="sections">
    <section class="job-section saved-jobs-section">
      <h2>Saved <i class="fas fa-bookmark"></i></h2>
      <div class="saved-job-cards">
        <div v-if="savedJobs.length === 0" class="no-jobs">No saved jobs yet.</div>
        <div v-else class="saved-job-cards-container">
          <div v-for="job in savedJobs" :key="job.id" class="saved-job-card" @click="selectJob(job)"> 
            <span :title="job.title">{{ shortenTitle(job.title) }}</span>
          </div>
        </div>
      </div>
    </section>

            <section class="job-section">
              <h2>Applied  <i class="fas fa-check-circle"></i> </h2>
              <JobList :jobs="appliedJobs" @update-job="updateJob" />
            </section>
            <section class="job-section">
              <h2>In Progress <i class="fas fa-spinner"></i></h2>
              <JobList :jobs="inProgressJobs" @update-job="updateJob" />
            </section>
          </div>
        </section>


        <!-- Job Statuses -->
      <section class="job-statuses">
          <h2>Job Statuses</h2>
          <ul>
            <li><i class="fas fa-bookmark"></i> Saved:({{ savedJobs.length }})</li>
            <li><i class="fas fa-spinner"></i> In Progress: {{ jobStatusCount('in-progress') }}</li>
            <li><i class="fas fa-check-circle"></i> Applied: {{ jobStatusCount('applied') }}</li>
            <li><i class="fas fa-envelope"></i> Awaiting Response: {{ jobStatusCount('awaiting-response') }}</li>
          </ul>
        </section>
      </div>
    </div>

    <!-- Job Details Modal -->
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <span @click="showModal = false" class="close">&times;</span>
        <h2>{{ selectedJob.title }}</h2>
        <p><strong>Company:</strong> {{ selectedJob.company }}</p>
        <p><strong>Location:</strong> {{ selectedJob.location }}</p>
        <p><strong>Type:</strong> {{ selectedJob.type }}</p>
        <p><strong>Posted:</strong> {{ selectedJob.posted }}</p>
        <div class="job-description">
          <p><strong>Description:</strong></p>
          <p>{{ selectedJob.description }}</p>
        </div>
        <p><strong>Category:</strong> {{ selectedJob.category }}</p>
        <p><strong>Salary:</strong> {{ selectedJob.salary }}</p>
        <p><strong>Contract Time:</strong> {{ selectedJob.contract_time }}</p>
        <p><strong>Redirect URL:</strong> <a :href="selectedJob.redirect_url">{{ selectedJob.redirect_url }}</a></p>
        <p><strong>Company URL:</strong> <a :href="selectedJob.company_url">{{ selectedJob.company_url }}</a></p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Hero from '@/components/Hero.vue';
import JobList from '@/components/JobList.vue';

export default {
  name: 'HomePage',
  components: {
    Hero,
    JobList,
  },
  data() {
    return {
      jobs: [],
      filteredJobs: [],
      savedJobs: [], //array to store saved jobs
      selectedJob: null,
      showModal: false,
    };
  },
  computed: {
    computed: {
    ...mapState(['jobs', 'savedJobs', 'filteredJobs']),
  },
    appliedJobs() {
      return this.jobs.filter(job => job.status === 'applied');
    },
    inProgressJobs() {
      return this.jobs.filter(job => job.status === 'in-progress');
    },
    awaitingResponseJobs() {
      return this.jobs.filter(job => job.status === 'awaiting-response');
    },
  },
  methods: {
    handleSearch(searchTerm) {
      this.filteredJobs = this.jobs.filter(job =>
        (job.title?.toLowerCase() || '').includes(searchTerm.toLowerCase()) ||
        (job.company?.toLowerCase() || '').includes(searchTerm.toLowerCase())
      );
    },
    shortenTitle(title) {
      const maxLength = 30; 
      if (title.length > maxLength) {
        return title.substring(0, maxLength) + "...";
      }
      return title;
    },
    handleJobSaved(job) {
      // add job to savedJobs array only if it doesn't already exist (i may need to review this)
      if (!this.savedJobs.find(savedJob => savedJob.id === job.id)) {
        this.savedJobs.push(job);
      }
    },
    applyForJob(job) {
      //i'll add logic to apply for a job later
      console.log(`Applying for job: ${job.title}`);
    },
    fetchJobs() {
      // fetch jobs when component is created
      const API_KEY = 'c5ac254dbcd7ffd334a80c341683b63e';
      const API_URL = `https://api.adzuna.com/v1/api/jobs/za/search/1?app_id=8b4326c4&app_key=${API_KEY}&results_per_page=100`;

      fetch(API_URL)
        .then(response => response.json())
        .then(data => {
          this.jobs = data.results.map(job => ({
            id: job.id,
            title: job.title,
            company: job.company.display_name,
            location: job.location.display_name,
            type: job.contract_type,
            description: job.description,
            category: job.category.label,
            salary: job.salary,
            posted: job.created,
            contract_time: job.contract_time,
            latitude: job.latitude,
            longitude: job.longitude,
            redirect_url: job.redirect_url,
            company_url: job.company.url,
            companyLogo: job.company.company_logo, 
          }));
          this.filteredJobs = this.jobs; // initialize filtered jobs with all jobs
        })
        .catch(error => console.error(error));
    },
    selectJob(job) {
      this.selectedJob = job;
      this.showModal = true;
    },
    jobStatusCount(status) {
      return this.jobs.filter(job => job.status === status).length;
    },
    // method to save a job
    saveJob(job) {
      // check if the job is already saved
      if (!this.savedJobs.find(savedJob => savedJob.id === job.id)) {
        this.savedJobs.push(job);
      }
    },
  },
  created() {
    this.fetchJobs(); 
  },

};
</script>



<style>
.nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #42b983;
  padding: 15px 20px;
  margin-top: -50px;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #fff;
}

.nav-links {
  display: flex;
}

.nav-link {
  display: flex;
  align-items: center;
  font-weight: bold;
  color: #fff;
  text-decoration: none;
  margin: 0 15px;
}

.nav-link.router-link-active {
  text-decoration: underline;
}

.btn {
  border-radius: 3px;
  padding: 8px 15px;
  transition: background-color 0.3s ease;
}

.btn-login {
  background-color: #fff;
  color: #42b983;
  margin-right: 10px;
}

.btn-signup {
  background-color: #fff;
  color: #42b983;
}

.btn:hover {
  background-color: #f8efc3;
}

.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.main-content {
  display: flex;
  margin-top: 20px;
  margin-left: 10px;
}

.job-listings,
.job-statuses {
  flex: 1;
  padding: 20px;
  margin-right: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.empty-section {
  flex: 2;
  padding: 20px;
  margin-right: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 50%;
}

.job-statuses-row {
  display: flex;
  flex-wrap: wrap;
}

.job-status {
  flex: 1;
  padding: 10px;
}


.section-title {
  color: #333;
}

.details-card {
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.job-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.job-info {
  margin-top: 20px;
}

.job-description {
  margin-top: 20px;
}

.job-actions {
  margin-top: 20px;
}

.company-logo {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.saved-jobs {
  flex: 1;
  padding: 20px;
  margin-right: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.saved-job-cards {
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.saved-job-card {
  padding: 20px;
  border-radius: 10px;             
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); 
  background-color: #fff;
  transition: all 0.3s ease; 
  cursor: pointer;
  margin-right: 20px;
  margin-bottom: 20px; 
}

.saved-job-card:last-child { 
  margin-right: 0;
}

.saved-job-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  transform: translateY(-3px); 
  background-color: #f5f5f5;
}

.sections {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.empty-section {
  flex: 2;
  padding: 20px;
  margin-right: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 50%; 
}

.empty-section h2{
  text-align: center;
  margin-bottom: 20px;
}

.sections {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.job-section {
  flex: 1 1 40%;
  min-width: 280px;
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.saved-jobs-section { 
  order: -1; 
}

</style>
