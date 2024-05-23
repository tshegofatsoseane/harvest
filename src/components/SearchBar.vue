<template>
    <div class="search-bar">
      <div class="search-input">
        <input type="text" v-model="searchTerm" placeholder="Search for jobs..." />
        <button @click="search">Search</button>
      </div>
      <div class="filter">
        <select v-model="selectedFilter" @change="applyFilter">
          <option value="">All</option>
          <option value="location">Location</option>
          <option value="type">Job Type</option>
        </select>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchBar',
    data() {
      return {
        searchTerm: '',
        selectedFilter: '' // Initialize selected filter
      };
    },
    methods: {
      search() {
        this.$emit('search', this.searchTerm, this.selectedFilter); // Emit both search term and selected filter
      },
      applyFilter() {
        this.$emit('filter', this.selectedFilter); // Emit selected filter only
      }
    }
  };
  </script>
  
  <style scoped>
  .search-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .search-input {
    display: flex;
  }
  
  .search-input input {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px 0 0 5px; /* Rounded border on the left side */
  }
  
  .search-input button {
    padding: 10px 20px;
    font-size: 1rem;
    color: #fff;
    background-color: #4caf50;
    border: none;
    border-radius: 0 5px 5px 0; /* Rounded border on the right side */
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .search-input button:hover {
    background-color: #388e3c;
  }
  
  .filter select {
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-left: 10px;
    cursor: pointer;
  }
  
  .filter select:focus {
    outline: none;
  }
  </style>
  