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
      <h1>Profile</h1>
      <div class="profile-section">
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
      this.fetchProfile();
    },
    methods: {
      async fetchProfile() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/accounts/profile/');
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
  
  .profile-section {
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
  }
  
  .profile-info p {
    margin: 5px 0;
  }
  </style>
  