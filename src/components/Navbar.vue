<template>
    <nav class="navbar">
      <div class="container">
        <router-link to="/" class="logo">YourApp</router-link>
        <ul class="nav-links">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/jobs">Jobs</router-link></li>
          <li><router-link to="/profile">Profile</router-link></li>
          <!-- Add more navigation links as needed -->
        </ul>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    name: 'NavbarComponent',
  };
  </script>
  
  <style scoped>
  .navbar {
    background-color: #42b983; /* Updated background color */
    color: #fff;
    padding: 15px 0; /* Increased padding for better spacing */
  }
  
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .logo {
    font-size: 1.8rem; /* Increased font size */
    font-weight: bold;
    color: #fff;
    text-decoration: none;
  }
  
  .nav-links {
    list-style: none;
    display: flex;
    margin: 0;
    padding: 0;
  }
  
  .nav-links li {
    margin-right: 30px; /* Increased margin between navigation items */
  }
  
  .nav-links li:last-child {
    margin-right: 0;
  }
  
  .nav-links li a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s; /* Added transition for smooth color change */
  }
  
  .nav-links li a:hover {
    color: #fff; /* Keep the same color on hover */
    opacity: 0.8; /* Reduced opacity on hover for visual effect */
  }
  </style>
  