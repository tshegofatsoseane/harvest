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
      selectedFilter: ''
    };
  },
  methods: {
    search() {
      this.$emit('search', this.searchTerm, this.selectedFilter);
    },
    applyFilter() {
      this.$emit('filter', this.selectedFilter);
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
  border: 1px solid #ddd;
  border-radius: 5px;
}

.search-input input {
  padding: 10px;
  font-size: 1rem;
  border: none;
  border-radius: 5px 0 0 5px;
  outline: none;
}

.search-input button {
  padding: 10px 20px;
  font-size: 1rem;
  color: #fff;
  background-color: #42b983;
  border: none;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  transition: background-color 0.3s ease;
  outline: none;
}

.search-input button:hover {
  background-color: #368753;
}

.filter select {
  padding: 10px;
  font-size: 1rem;
  border: none;
  border-left: 1px solid #ddd; 
  border-radius: 0 5px 5px 0; 
  cursor: pointer;
  outline: none;
}

.filter select:focus {
  outline: none;
}
</style>
