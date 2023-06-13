<template>
  <div id="app">
    <nav class="navbar">
      <div class="navbar-brand">
        <span class="navbar-title">Babel Store</span>
      </div>
      <div class="navbar-links">
        <router-link to="/" class="navbar-link">Home</router-link>
        <router-link to="/login" class="navbar-link">Login</router-link>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navbar {
  padding: 30px;
  background-color: #f5f5f5;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-brand {
  font-weight: bold;
}

.navbar-title {
  font-size: 24px;
  color: #2c3e50;
}

.navbar-links {
  display: flex;
}

.navbar-link {
  font-weight: bold;
  color: #2c3e50;
  margin-left: 1.5rem;
  text-decoration: none;
}

.navbar-link.router-link-exact-active {
  color: #42b983;
}
</style>
