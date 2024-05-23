<template>
    <div class="home-page">
      <Hero @search="handleSearch" />
      <div class="main-content">
        <section class="job-listings">
          <h2>Job Listings</h2>
          <JobList :jobs="filteredJobs" />
        </section>
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
        const API_URL = `https://api.adzuna.com/v1/api/jobs/za/search/1?app_id=8b4326c4&app_key=${API_KEY}&results_per_page=9&what=software%20engineering%20intern&what_and=software%20engineering%20intern`;
        
  
        fetch(API_URL)
          .then(response => response.json())
          .then(data => {
            this.jobs = data.results.map(job => ({
              id: job.id,
              title: job.title,
              company: job.company.display_name,
              location: job.location.display_name,
              type: job.contract_type,
            }));
            this.filteredJobs = this.jobs; // Initialize filtered jobs with all jobs
          })
          .catch(error => console.error(error));
      },
    },
    created() {
      this.fetchJobs(); // Fetch jobs when component is created
    },
  };
  </script>
  
  <style>
  .home-page {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  header {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .main-content {
    display: flex;
    width: 100%;
    max-width: 1200px;
  }
  
  .job-listings {
    flex: 3;
  }
  </style>
  