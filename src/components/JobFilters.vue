<template>
    <div class="job-filters">
      <h3 class="filter-title">Filter Jobs</h3>
      <div class="filter-group">
        <label for="location" class="filter-label">Location:</label>
        <select id="location" v-model="filters.location" @change="onFilter" class="filter-select">
          <option value="">All</option>
          <option value="New York">Joburg</option>
          <option value="San Francisco">Capetown</option>
        </select>
      </div>
      <div class="filter-group">
        <label for="type" class="filter-label">Job Type:</label>
        <select id="type" v-model="filters.type" @change="onFilter" class="filter-select">
          <option value="">All</option>
          <option value="Full-time">Full-time</option>
          <option value="Part-time">Part-time</option>
        </select>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'JobFilters',
    data() {
      return {
        filters: {
          location: '',
          type: '',
        },
      };
    },
    methods: {
      onFilter() {
        this.$emit('filter', this.filters);
      },
    },
  };
  </script>
  
  <style>
  .job-filters {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    background-color: #f0f4f8;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 20px;
  }
  
  .filter-title {
    flex: 0 0 100%;
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 10px;
  }
  
  .filter-group {
    margin-right: 10px;
  }
  
  .filter-label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .filter-select {
    padding: 10px;
    font-size: 16px;
    border-radius: 5px;
    border: 1px solid #ddd;
    background-color: #fff;
  }
  
  .filter-select:focus {
    outline: none;
    border-color: #42b983;
  }
  </style>
  