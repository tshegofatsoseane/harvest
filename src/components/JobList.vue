<template>
  <div class="job-list">
    <div v-if="jobs.length === 0" class="no-jobs">No jobs found.</div>
    <div v-for="job in jobs" :key="job.id" class="job-card">
      <h3>{{ job.title }}</h3>
      <p>{{ job.company }}</p>
      <div class="job-details">
        <p class="location"><i class="fas fa-map-marker-alt"></i> {{ job.location }}</p>
        <p class="type"><i class="fas fa-briefcase"></i> {{ job.type }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'JobList',
  props: {
    jobs: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.job-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.job-card {
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  transition: transform 0.3s ease;
}

.job-card:hover {
  transform: translateY(-5px);
}

.job-card h3 {
  margin: 0 0 10px;
  color: #333;
}

.job-card p {
  margin: 5px 0;
  color: #666;
}

.job-details {
  display: flex;
  justify-content: space-between;
}

.location,
.type {
  font-size: 14px;
  font-weight: bold;
  text-transform: uppercase;
}

/* Font Awesome icons */
.job-details i {
  margin-right: 5px;
  color: #42b983;
}
</style>
