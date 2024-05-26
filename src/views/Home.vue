<template>
  <div>
    <nav class="nav">
      <div class="logo">Harvest</div>
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
    <div class="home-page">
      <Hero @search="handleSearch" />
      <div class="main-content">
        <section class="job-listings">
          <h2>Job Listings</h2>
          <JobList :jobs="filteredJobs" @selectJob="selectJob" />
        </section>
        <section class="job-details">
          <h2>Job Details</h2>
          <div v-if="selectedJob" class="details-card">
            <h3>{{ selectedJob.title }}</h3>
            <p><strong>Company:</strong> {{ selectedJob.company }}</p>
            <p><strong>Location:</strong> {{ selectedJob.location }}</p>
            <p><strong>Type:</strong> {{ selectedJob.type }}</p>
            <p><strong>Description:</strong> {{ selectedJob.description }}</p>
          </div>
          <div v-else>
            <p>Select a job to see the details.</p>
          </div>
        </section>
        <section class="job-statuses">
          <h2>Job Statuses</h2>
          <ul>
            <li>Saved: {{ jobStatusCount('saved') }}</li>
            <li>In Progress: {{ jobStatusCount('in-progress') }}</li>
            <li>Applied: {{ jobStatusCount('applied') }}</li>
            <li>Awaiting Response: {{ jobStatusCount('awaiting-response') }}</li>
          </ul>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
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
      selectedJob: null,
    };
  },
  methods: {
    handleSearch(searchTerm) {
      this.filteredJobs = this.jobs.filter(job =>
        (job.title?.toLowerCase() || '').includes(searchTerm.toLowerCase()) ||
        (job.company?.toLowerCase() || '').includes(searchTerm.toLowerCase())
      );
    },
    fetchJobs() {
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
            description: job.description, // Assuming the API returns a description field
          }));
          this.filteredJobs = this.jobs; // Initialize filtered jobs with all jobs
        })
        .catch(error => console.error(error));
    },
    selectJob(job) {
      this.selectedJob = job;
    },
    jobStatusCount(status) {
      return this.jobs.filter(job => job.status === status).length;
    },
  },
  created() {
    this.fetchJobs(); // Fetch jobs when component is created
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
  width: 100%;
  max-width: 1500px;
  margin-top: 20px;
}

.job-listings {
  flex: 1;
  padding: 20px;
  margin-left: 0; /* Remove left margin */
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.job-details {
  flex: 3; /* Increase the flex value to give more width */
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 0 20px;
}

.job-statuses {
  flex: 1;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.details-card {
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>
