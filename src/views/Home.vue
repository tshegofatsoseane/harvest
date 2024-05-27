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
          <JobList :jobs="filteredJobs" @selectJob="selectJob" @jobSaved="handleJobSaved" @jobinProgress="handleJobinProgress" />
        </section>

        <section class="empty-section">
          <h2>Job Statuses</h2>
          <div class="sections">

<section class="job-section saved-jobs-section">
  <h2>Saved <i class="fas fa-bookmark"></i></h2>
  <div class="saved-job-cards">
    <div v-if="savedJobs.length === 0" class="no-jobs">No saved jobs yet.</div>
    <div v-else class="saved-job-cards-container">
      <div v-for="job in savedJobs" :key="job.id" class="saved-job-card">
        <div class="card-content">
          <h3> <span :title="job.title">{{ shortenTitle(job.title) }}</span> </h3>
          <p>{{ job.company }}</p>
          <div class="card-buttons">
            <button class="icon-button" @click="selectJob(job)">
              <i class="fas fa-eye"></i>
            </button>
            <button class="icon-button" @click.stop="showDeleteConfirmation(job)">
              <i class="fas fa-trash"></i>
            </button>
            <button class="icon-button" @click="togglePopover(job)">
              <i class="fas fa-ellipsis-v"></i>
            </button>
          </div>
        </div>
        <div v-if="job === showPopoverForJob" class="popover">
          <button @click="updateJobStatus(job, 'applied')">Applied</button>
          <button @click="handleJobinProgress(job, 'in-progress')">In Progress</button>
          <button @click="updateJobStatus(job, 'awaiting-response')">Awaiting Response</button>
          <button @click="updateJobStatus(job, 'interview')">Interview</button>
        </div> 
      </div>
    </div>
  </div>
</section>



<div v-if="showDeleteModal" class="modal">
  <div class="modal-content">
    <p>Are you sure you want to delete this saved job?</p>
    <button @click="deleteSavedJob">Yes</button>
    <button @click="showDeleteModal = false">No</button>
  </div>
</div>

    <section class="job-section inprogress-jobs-section">
    <h2>In Progress <i class="fas fa-spinner"></i></h2>
    <div v-if="inprogressJobs.length === 0" class="no-jobs"  @jobSaved="handleJobSaved" >No saved jobs yet.</div>
    <div v-else class="saved-job-cards-container">
      <div v-for="job in inprogressJobs" :key="job.id" class="saved-job-card">
        <div class="card-content">
          <h3> <span :title="job.title">{{ shortenTitle(job.title) }}</span> </h3>
          <p>{{ job.company }}</p>
          <div class="card-buttons">
            <button class="icon-button" @click="selectJob(job)">
              <i class="fas fa-eye"></i>
            </button>
            <button class="icon-button" @click.stop="showDeleteConfirmation(job)">
              <i class="fas fa-trash"></i>
            </button>
            <button class="icon-button" @click="togglePopover(job)">
              <i class="fas fa-ellipsis-v"></i>
            </button>
          </div>
        </div>
        <div v-if="job === showPopoverForJob" class="popover">
          <button @click="updateJobStatus(job, 'applied')">Applied</button>
          <button @click="handleJobinProgress(job, 'in-progress')">In Progress</button>
          <button @click="updateJobStatus(job, 'awaiting-response')">Awaiting Response</button>
          <button @click="updateJobStatus(job, 'interview')">Interview</button>
        </div>
      </div>
    </div>
            </section>
            
            <section class="job-section applied-jobs-section">
              <h2>Applied  <i class="fas fa-check-circle"></i> </h2>
              <JobList :jobs="appliedJobs" @update-job="updateJob" />
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
import { mapState, mapActions } from 'vuex';
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
      inprogressJobs: [], //array to store inprogress jobs
      selectedJob: null,
      showModal: false,
      showDeleteModal: false,
      jobToDelete: null,
      showPopoverForJob: null,
    };
  },
  computed: {
    computed: {
    ...mapState(['jobs', 'savedJobs', 'inprogressJobs',  'filteredJobs']),
    ...mapActions(['updateJob']),
    toggleprogress(job) {
      const newStatus = !job.progressed;
      this.updateJob({
        jobId: job.id,
        newStatus,
        isInprogress: newStatus,
      });
      this.$emit('jobinProgress', job); // emit jobinProgress event
    }
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
    togglePopover(job) {
      this.showPopoverForJob = this.showPopoverForJob === job ? null : job;
    },
    updateJobStatus(job, newStatus) {
      job.status = newStatus;
      this.$store.commit('updateJob', job);
      this.togglePopover(job); // Close popover after updating status
      // I'll add logic to close popover if status not updated

      if (newStatus === 'in-progress') {
      this.inProgressJobs.push(job);
      this.savedJobs = this.savedJobs.filter(j => j.id !== job.id);
    } 
    },
    showDeleteConfirmation(job) {
      this.jobToDelete = job;
      this.showDeleteModal = true;
    },
    deleteSavedJob() {
      if (this.jobToDelete) {
        const index = this.savedJobs.indexOf(this.jobToDelete);
        if (index > -1) {
          this.savedJobs.splice(index, 1);
        }
        this.showDeleteModal = false;
        this.jobToDelete = null;
      }
    },
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

    handleJobinProgress(job, newStatus) {
      // add job to inprogress array
      if (!this.inprogressJobs.find(inProgressJob => inProgressJob.id === job.id)) {
        job.status = newStatus;
        this.$store.commit('updateJob', job);
        this.inprogressJobs.push(job);
        this.togglePopover(job);
        this.savedJobs.pop(job);
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
    inProgressJob(job) {
      // check if the job is already inprogress
      if (!this.inProgressJobs.find(inProgressJob => inProgressJob.id === job.id)) {
        this.inProgressJobs.push(job);
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
  width: 30%;
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
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  transition: transform 0.3s ease;
  cursor: pointer;
  display: flex; 
  flex-direction: column; 
  width: 270px;
  margin-left: -5px;
}

.saved-job-card .card-content {
  align-items: center;
}

.saved-job-card .card-buttons {
  display: flex; 
}

.saved-job-card .icon-button {
  background-color: white;
  border: 2px solid #388e3c;
  color: #388e3c;
  border-radius: 10px;
  width: 30px;
  height: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.saved-job-card .icon-button:hover {
  background-color: #f0f0f0;
}

.saved-job-card:last-child { 
  margin-right: 0;
}

.saved-job-card:hover {
  transform: translateY(-5px);
}

.saved-job-card h3 {
  margin: 0 0 10px;
  color: #333;
}

.saved-job-card p {
  margin: 5px 0;
  color: #666;
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
  background-color: #fff; 
  border-radius: 10px; 
}

.saved-jobs-section h2 {
  color: #388e3c; 
  font-size: 1.2rem;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.inprogress-jobs-section h2 {
  color: #388e3c; 
  font-size: 1.2rem;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.applied-jobs-section h2 {
  color: #388e3c; 
  font-size: 1.2rem;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  gap: 5px;
}

.saved-job-cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
  gap: 20px;
}

.popover {
  position: absolute;
  top: 100%; 
  right: 0;
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
  z-index: 10;
}

.popover button {
  display: block;
  width: 100%;
  background-color: green;
  border: none;
  padding: 8px;
  text-align: left; 
  cursor: pointer;
  margin-bottom: 5px;
}

</style>

