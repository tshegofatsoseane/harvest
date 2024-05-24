<template>
    <div>
  
     <nav class="nav">
        <div class="logo">Harvest</div>
        <div class="nav-links">
          <router-link to="/" class="nav-link">
            <i class="fas fa-home"></i> Home
          </router-link>
          <router-link to="/profile" class="nav-link">
            <i class="fas fa-user"></i> Profile
          </router-link>
          <router-link to="/jobs" class="nav-link">
            <i class="fas fa-briefcase"></i> Jobs
          </router-link>
          <router-link to="/login" class="btn btn-login">
            <i class="fas fa-sign-in-alt"></i> Login
          </router-link>
          <router-link to="/signup" class="btn btn-signup">
            <i class="fas fa-user-plus"></i> Signup
          </router-link>
        </div>
      </nav>
        
<div class="profile-page">
    <h1 class="page-title">Profile</h1>
    <div class="profile-card">
      <div class="profile-card-content">
        <div class="profile-picture">
          <img :src="profile.picture" alt="Profile Picture">
        </div>
        <div class="profile-info">
          <p><strong>Username:</strong> {{ profile.username }}</p>
          <p><strong>Email:</strong> {{ profile.email }}</p>
          <p><strong>Bio:</strong> {{ profile.bio }}</p>
          <p><strong>Location:</strong> {{ profile.location }}</p>
          <p><strong>Birth Date:</strong> {{ profile.birth_date }}</p>
        </div>
      </div>
    </div>
  </div>
    </div>


  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'ProfilePage',
    data() {
      return {
        profile: {
          picture: '',
          username: '',
          email: '',
          bio: '',
          location: '',
          birth_date: ''
        }
      };
    },
    created() {
      // Call the function to fetch profile with token included in headers
      this.fetchProfileWithToken();
    },
    methods: {
      async fetchProfileWithToken() {
        try {
          // Get the token from localStorage (assuming you store it there after login)
          const token = localStorage.getItem('token');
  
          // Include the token in the request headers
          const response = await axios.get('http://127.0.0.1:8000/api/accounts/profile/', {
            headers: {
              Authorization: `Bearer ${token}` // Add the token to the Authorization header
            }
          });
  
          // Update the profile data
          this.profile = response.data;
        } catch (error) {
          console.error('Failed to fetch profile:', error);
        }
      }
    }
  };
  </script>
  <style>
  .profile-page {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.page-title {
  font-size: 24px;
  color: #009345; /* App's primary color */
  margin-bottom: 20px;
}

.profile-card {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.profile-card:hover {
  transform: translateY(-5px);
}

.profile-card-content {
  padding: 20px;
  display: flex;
  align-items: center;
}

.profile-picture {
  margin-right: 20px;
}

.profile-picture img {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-info p {
  margin: 5px 0;
  color: #333; /* Text color */
}

.profile-info strong {
  color: #009345; /* App's primary color */
}
  </style>
  