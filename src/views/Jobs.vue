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
    
      <div class="jobs-page">
      <h1 class="page-title">Jobs</h1>
      <div class="sections">
        <section class="job-section">
          <h2>Saved</h2>
          <JobList :jobs="savedJobs" @update-job="updateJob" /> 
        </section>
        <section class="job-section">
          <h2>Applied</h2>
          <JobList :jobs="appliedJobs" @update-job="updateJob" />
        </section>
        <section class="job-section">
          <h2>In Progress</h2>
          <JobList :jobs="inProgressJobs" @update-job="updateJob" />
        </section>
        </div>
    </div>

  </div>
</template>

<script>
import { mapState } from 'vuex';
import JobList from '@/components/JobList.vue';

export default {
  name: 'JobsPage',
  components: { JobList },
  computed: {
    ...mapState(['jobs']),
    savedJobs() {
      return this.jobs.filter(job => job.saved);
    },
    appliedJobs() {
      return this.jobs.filter(job => job.status === 'applied');
    },
    inProgressJobs() {
      return this.jobs.filter(job => job.status === 'in-progress');
    },
  },
  methods: {
    updateJob(updatedJob) {
      this.$store.commit('updateJob', updatedJob);
    },
  },
  created() {
    this.$store.dispatch('fetchJobs');
  },
};
</script>

<style scoped>
.jobs-page {
  max-width: 1200px;
  margin: auto;
  padding: 20px;
}

.page-title {
  font-size: 24px;
  color: #009345;
  margin-bottom: 20px;
}

.sections {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.job-section {
  flex: 1;
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>