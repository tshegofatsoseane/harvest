<template>
    <nav class="navbar">
      <div class="container">
        <router-link to="/" class="logo">YourApp</router-link>
        <ul class="nav-links">
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/jobs">Jobs</router-link></li>
          <li><router-link to="/profile">Profile</router-link></li>
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
    background-color: #42b983; 
    color: #fff;
    padding: 15px 0; 
  }
  
  .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  .logo {

    font-size: 1.8rem;
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
    margin-right: 30px;
  }
  
  .nav-links li:last-child {
    margin-right: 0;
  }
  
  .nav-links li a {
    color: #fff;
    text-decoration: none;

    transition: color 0.3s; 
  }
  
  .nav-links li a:hover {
    color: #fff; 
    opacity: 0.8; 

  }
  </style>
  