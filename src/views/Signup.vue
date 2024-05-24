<template>
    <div class="center-container">
      <article>
        <div class="container" :class="{'sign-up-active': signUp}">
          <div class="overlay-container" :class="{'shift-left': signUp}">
            <div class="overlay">
              <div class="overlay-left">
                <h2>Welcome Back!</h2>
                <p>Please login with your personal info</p>
                <button class="invert" id="signIn" @click="signUp = false">Sign In</button>
              </div>
              <div class="overlay-right">
                <h2>Hello, Friend!</h2>
                <p>Please enter your personal details</p>
                <button class="invert" id="signUp" @click="signUp = true">Sign Up</button>
              </div>
            </div>
          </div>
          <form class="sign-up" @submit.prevent="handleSignUp" v-show="signUp">
            <h2>Create login</h2>
            <div>Use your email for registration</div>
            <input type="text" v-model="signUpForm.name" placeholder="Name" />
            <input type="email" v-model="signUpForm.email" placeholder="Email" />
            <input type="password" v-model="signUpForm.password" placeholder="Password" />
            <button type="submit">Sign Up</button>
          </form>
          <form class="sign-in" @submit.prevent="handleSignIn" v-show="!signUp">
            <h2>Sign In</h2>
            <div>Use your account</div>
            <input type="text" v-model="signInForm.name" placeholder="Username" />
            <input type="password" v-model="signInForm.password" placeholder="Password" />
            <a href="#">Forgot your password?</a>
            <button type="submit">Sign In</button>
          </form>
        </div>
      </article>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'SignupPage',
    data() {
      return {
        signUp: false,
        signUpForm: {
          name: '',
          email: '',
          password: ''
        },
        signInForm: {
          email: '',
          password: ''
        }
      };
    },
    setup() {
      const router = useRouter();
      return { router };
    },
    methods: {
      async handleSignUp() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/accounts/signup/', {
            username: this.signUpForm.name,
            email: this.signUpForm.email,
            password: this.signUpForm.password
          });
  
          if (response && response.data) {
            console.log(response.data);
            alert('Sign up successful! Please sign in.');
            this.signUp = false;
          } else {
            console.error('Unexpected response structure', response);
            alert('Sign up failed due to unexpected response structure.');
          }
        } catch (error) {
          if (error.response && error.response.data) {
            console.error(error.response.data);
            alert(`Sign up failed: ${error.response.data.detail || 'Unknown error'}`);
          } else {
            console.error('Network or server error', error);
            alert('Sign up failed due to a network or server error.');
          }
        }
      },
      async handleSignIn() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/accounts/login/', {
            username: this.signInForm.name,
            password: this.signInForm.password
          });
  
          if (response && response.data) {
            console.log(response.data);
            alert('Sign in successful!');
            // Redirect to homepage on successfull login
            this.$router.push('/');
          } else {
            console.error('Unexpected response structure', response);
            alert('Sign in failed due to unexpected response structure.');
          }
        } catch (error) {
          if (error.response && error.response.data) {
            console.error(error.response.data);
            alert(`Sign in failed: ${error.response.data.detail || 'Unknown error'}`);
          } else {
            console.error('Network or server error', error);
            alert('Sign in failed due to a network or server error.');
          }
        }
      }
    }
  };
  </script>
  
  <style>
  /* Styles are the same as you provided */
  .center-container {
    margin-top: -50px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f8efc3; /* Set background color here */
  }
  
  .container {
    position: relative;
    width: 1200px;
    height: 580px;
    border-radius: 10px;
    overflow: hidden;
  }
  
  .overlay-container {
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform .5s ease-in-out;
    z-index: 100;
  }
  
  .overlay {
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    background: #42b983;
    color: #fff;
    transform: translateX(0);
    transition: transform .5s ease-in-out;
  }
  
  .overlay-left {
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
    padding: 70px 40px;
    width: calc(50% - 80px);
    height: calc(100% - 140px);
    text-align: center;
    transform: translateX(-20%);
    transition: transform .5s ease-in-out;
  }
  
  .overlay-right {
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
    padding: 70px 40px;
    width: calc(50% - 80px);
    height: calc(100% - 140px);
    text-align: center;
    transform: translateX(0);
    right: 0;
    transition: transform .5s ease-in-out;
  }
  
  h2 {
    margin: 0;
  }
  
  p {
    margin: 20px 0 30px;
  }
  
  a {
    color: #222;
    text-decoration: none;
    margin: 15px 0;
    font-size: 1rem;
  }
  
  button {
    border-radius: 20px;
    border: 1px solid #009345;
    background-color: #009345;
    color: #fff;
    font-size: 1rem;
    font-weight: bold;
    padding: 10px 40px;
    letter-spacing: 1px;
    text-transform: uppercase;
    cursor: pointer;
    transition: transform .1s ease-in;
  }
  
  button:active {
    transform: scale(.9);
  }
  
  button:focus {
    outline: none;
  }
  
  button.invert {
    background-color: transparent;
    border-color: #fff;
  }
  
  form {
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
    padding: 90px 60px;
    width: calc(50% - 120px);
    height: calc(100% - 180px);
    text-align: center;
    background: white;
    transition: all .5s ease-in-out;
  }
  
  div {
    font-size: 1rem;
  }
  
  input {
    background-color: #eee;
    border: none;
    padding: 8px 15px;
    margin: 6px 0;
    width: calc(100% - 30px);
    border-radius: 15px;
    border-bottom: 1px solid #ddd;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, .4), 0 -1px 1px #fff, 0 1px 0 #fff;
    overflow: hidden;
  }
  
  input:focus {
    outline: none;
    background-color: #fff;
  }
  
  /* Shift overlay to the left */
  .shift-left .overlay-container {
    transform: translateX(-100%);
  }
  </style>
  