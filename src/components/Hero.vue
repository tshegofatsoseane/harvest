<template>
    <div class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">Welcome to Harvest</h1>
        <p class="hero-subtitle">Find your dream job today</p>
        <SearchBar @search="handleSearch" />
      </div>
    </div>
  </template>
  
  <script>
  import SearchBar from '@/components/SearchBar.vue';
  
  export default {
    name: 'HeroSection',
    components: {
      SearchBar
    },
    methods: {
      handleSearch(searchTerm) {
        this.$emit('search', searchTerm);
      }
    }
  };
  </script>
  
  <style scoped>
  .hero-section {
    background-color: #f8efc3;
    padding: 80px 0;
    text-align: center;
    width: 100%;
  }
  
  .hero-content {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .hero-title {
    font-size: 3rem;
    margin-bottom: 20px;
    color: #333;
  }
  
  .hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: 40px;
    color: #666;
  }
  
  .btn-primary {
    padding: 12px 24px;
    font-size: 1rem;
    color: #fff;
    background-color: #4caf50;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .btn-primary:hover {
    background-color: #388e3c;
  }
  </style>
  