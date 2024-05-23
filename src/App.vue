<template>
  <div id="app">
    <nav>
      <div class="logo">Harvest</div> <!-- Logo -->
      <div class="nav-links">
        <router-link to="/">
          <i class="fas fa-home"></i> Home
        </router-link>
        <router-link to="/profile">
          <i class="fas fa-user"></i> Profile
        </router-link>
        <router-link to="/jobs">
          <i class="fas fa-briefcase"></i> Jobs
        </router-link>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  display: flex; /* Use flexbox */
  justify-content: space-between; /* Align items horizontally */
  align-items: center; /* Align items vertically */
  background-color: #42b983; /* Background color */
  padding: 15px 20px; /* Padding top and bottom */
  margin-top: -50px;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #fff;
}

.nav-links {
  display: flex;
}

.nav-links router-link {
  display: flex;
  align-items: center;
  font-weight: bold;
  color: #fff; /* Text color */
  text-decoration: none;
  margin: 0 15px;
}

.nav-links router-link.router-link-active {
  text-decoration: underline; /* Underline active link */
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #fff;
  margin-right: 20px; /* Add margin to separate logo from links */
}

nav a {
  display: flex;
  align-items: center;
  font-weight: bold;
  color: #fff; /* Text color */
  text-decoration: none;
  margin: 0 15px;
}

nav a.router-link-active {
  text-decoration: underline; /* Underline active link */
}

nav i {
  margin-right: 8px; /* Space between icon and text */
}
</style>
