<link rel="stylesheet" style="text/css" href="../../static/login.css"/>

<template>
<div class="inFormBackground">
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="inLoginForm">
        <form v-on:submit.prevent="login">
            <div class="title">
                <h3>Login</h3>
            </div>
            <div class="inputGroup">
                <input
                    placeholder="Enter Email"
                    type="email"
                    class="form-control"
                    v-model="user.email"
                    id="email"
                    required
                    />
            </div>
            <div class="inputGroup">
                <input
                    placeholder="Enter Password"
                    type="password"
                    class="form-control"
                    v-model="user.passwd"
                    id="password"
                    required
                    />
            </div>
            <button class="submitForm">Log In</button>
            <router-link class="registerbtn" :to="{ name: 'register' }">
                Register here
            </router-link>
        </form>
    </div>
</div>
</template>

<script>
export default {
  data () {
    return {
      user: {}
    }
  },
  methods: {
    login: function () {
      this.$http
        .get('http://localhost:5000/listUsers', this.livro, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            var users = response.body
            console.log(users)
            if (users.length !== 0) {
              for (let i = 0; i < users.length; i++) {
                if (users[i].email === this.user.email) {
                  console.log('User already registered')
                  if (this.user.passwd === users[i].passwd) {
                    localStorage.setItem('user_info', JSON.stringify({'name': users[i].name, 'email': users[i].email, 'passwd': users[i].passwd}))
                    console.log('User logged in')
                    this.$router.push('list')
                    return true
                  } else {
                    console.log('Wrong password')
                    return false
                  }
                }
              }
              console.log('User is not registered')
              return false
            }
          },
          (response) => {
            alert(response.body['mensagem'])
          }
        )
    }
  }
}
</script>
