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
      <button @click="toggleSaved(job)" class="save-button" :class="{ saved: job.saved }">
        <i :class="job.saved ? 'fas fa-bookmark' : 'far fa-bookmark'"></i>
        {{ job.saved ? 'Saved' : 'Save' }}
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  props: {
    jobs: {
      type: Array,
      required: true,
    },
  },
  methods: {
    ...mapActions(['updateJob']),
    toggleSaved(job) {
      this.updateJob({
        jobId: job.id,
        newStatus: job.status,
        isSaved: !job.saved,
      });
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

.job-details i {
  margin-right: 5px;
  color: #42b983;
}

.save-button {
  display: flex;
  align-items: center;
  background-color: #fff;
  border: 2px solid #42b983;
  color: #42b983;
  border-radius: 5px;
  padding: 8px 15px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
  font-size: 14px;
}

.save-button:hover {
  background-color: #f0f0f0;
}

.save-button i {
  margin-right: 5px;
}

.save-button.saved {
  background-color: #42b983;
  color: #fff;
}

.save-button.saved i {
  color: #fff;
}

.no-jobs {
  text-align: center;
  color: #666;
  font-size: 18px;
  margin-top: 20px;
}
</style>
