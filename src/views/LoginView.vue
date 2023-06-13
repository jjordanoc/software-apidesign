<template>
  <div class="login">
    <div class="title">
      <h1>Login</h1>
    </div>

    <form class="form" @submit.prevent="login">

      <label class="form-label" htmlFor="username">Username:</label>
        <input
        v-model="username"
        name="username"
        class="form-input"
        type="text"
        id="username"
        required
        placeholder="Username"
      >

      <label class="form-label" htmlFor="password">Password:</label>
        <input
        v-model="password"
        name="password"
        class="form-input"
        type="password"
        id="password"
        required
        placeholder="Password"
      >

      <button class="form-submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
      try {
        const res = await axios.get('http://localhost:8002/user');

        // Handle successful login response here
        const usersList = JSON.parse(res.data).users;
        console.log(usersList);

        usersList.forEach((user) => {
          if (user.name === this.username && user.password === this.password) {
            this.$router.push('/');
          }
        });
      } catch (error) {
        // Handle login error here
        console.error(error);
        // Show error message, clear form fields, etc.
      }
    },
  },
};
</script>

<style scoped>
.login {
  padding: 2rem;
}

.title {
  text-align: center;
}

.form {
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 100%;
  max-width: 400px;
  background: #f5f5f5;
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}

.form-label {
  margin-top: 2rem;
  color: rgba(0, 0, 0, 0.9);
  margin-bottom: 0.5rem;
}

.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid #000;
  color: #000;
  transition: border-color 0.2s;
}

.form-input:focus {
  outline: none;
  border-color: #1ab188;
}

.form-submit {
  background: #1ab188;
  border: none;
  color: #fff;
  margin-top: 2rem;
  padding: 1rem 0;
  cursor: pointer;
  transition: background 0.2s;
}

.form-submit:hover {
  background: #0b9185;
}
</style>
