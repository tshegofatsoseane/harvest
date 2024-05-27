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
      <div class="actions">
        <button
          :class="['save-button', { saved: job.saved }]"
          @click.stop="toggleSave(job)">
          <i :class="job.saved ? 'fas fa-bookmark' : 'far fa-bookmark'"></i>
          {{ job.saved ? 'Saved' : 'Save' }}
        </button>
        <button class="view-details-button" @click="selectJob(job)">
          View Details
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'JobList',
  props: {
    jobs: {
      type: Array,
      required: true,
    },
  },
  methods: {
    ...mapActions(['updateJob']),
    toggleSave(job) {
      const newStatus = !job.saved;
      this.updateJob({
        jobId: job.id,
        newStatus,
        isSaved: newStatus,
      });
      this.$emit('jobSaved', job); // emit jobSaved event
    },
    selectJob(job) {
      this.$emit('selectJob', job);
    },
  },
};
</script>

<style scoped>
.job-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.job-card {
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  transition: transform 0.3s ease;
  cursor: pointer;
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

.actions {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
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

.view-details-button {
  background-color: #42b983;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 8px 15px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
  font-size: 14px;
}

.view-details-button:hover {
  background-color: #36a270;
}

.no-jobs {
  text-align: center;
  color: #666;
  font-size: 18px;
  margin-top: 20px;
}
</style>
