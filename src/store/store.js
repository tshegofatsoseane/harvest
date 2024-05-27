import { createStore } from 'vuex';
import axios from 'axios';

const apiUrl = 'http://127.0.0.1:8000/api/jobs/';

export default createStore({
  state: {
    jobs: [],
  },
  mutations: {
    setJobs(state, jobs) {
      state.jobs = jobs;
    },
    updateJobStatus(state, updatedJob) {
      const index = state.jobs.findIndex(job => job.id === updatedJob.id);
      if (index !== -1) {
        state.jobs.splice(index, 1, updatedJob);
      }
    },
  },
  actions: {
    fetchJobs({ commit }) {
      axios.get(apiUrl)
        .then(response => {
          commit('setJobs', response.data);
        })
        .catch(error => console.error(error));
    },
    saveJob({ dispatch }, job) {
      axios.post(apiUrl, job)
        .then(() => {
          dispatch('fetchJobs');
        })
        .catch(error => console.error(error));
    },
    updateJobStatus({ dispatch }, { id, status }) {
      axios.post(`${apiUrl}${id}/update_status/`, { status })
        .then(() => {
          dispatch('fetchJobs');
        })
        .catch(error => console.error(error));
    },
  },
});
