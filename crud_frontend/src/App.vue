<link rel="stylesheet" style="text/css" href="../../static/table_and_forms.css"/>
<link rel="stylesheet" style="text/css" href="../../static/app.css"/>

<template>
<div id="app">
    <nav class="navigationWrapper">
        <div class="navbarcontent">
            <div class="header">
                <div class="logoWrapper">
                    <span class="logo">Decadent</span>
                    <span class="stylish">Dishes</span>
                </div>
                <div class="header-menu">
                  <router-link class="btn btn-primary" :to="{ name: 'list' }"
                    >Find your recipe</router-link
                  >
                  <router-link v-bind:disabled="isButtonDisabled" class="btn btn-primary share-recipe" :to="{ name: 'create' }"
                    >Share a recipe</router-link
                  >
                </div>
                <router-link class="user-settings" :to="{ name: 'login' }">
                    <img class="user-profile" src="../src/assets/profile_icon.png" alt="profile_icon">
                    <div ref="user-name" class="user-name">Login</div>
                </router-link>
            </div>
        </div>
    </nav>
    <router-view />
</div>
</template>

<script>
export default {
  data () {
    return {
      user: [],
      isButtonDisabled: true
    }
  },

  beforeUpdate: function () {
    this.getUserData()
  },

  methods: {
    getUserData: function () {
      let user = JSON.parse(localStorage.getItem('user_info'))
      if (user !== null) {
        this.$el.querySelector('.user-name').innerText = user['name']
        this.$el.querySelector('.user-settings').to = { name: 'list' }
        this.isButtonDisabled = !this.isButtonDisabled
      } else {
        this.$el.querySelector('.user-name').innerText = 'Login'
        this.isButtonDisabled = true
      }
    }
  }
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
