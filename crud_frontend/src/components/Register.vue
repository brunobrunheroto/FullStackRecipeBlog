<link rel="stylesheet" style="text/css" href="../../static/login.css"/>

<template>
<div class="inFormBackground">
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="inLoginForm">
        <form v-on:submit.prevent="adduser">
            <div class="title">
                <h3>Register</h3>
            </div>
            <div class="inputGroup">
                <input
                    placeholder="Enter Name"
                    type="text"
                    class="form-control"
                    v-model="user.name"
                    id="name"
                    required
                    />
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
            <div class="inputGroup">
                <input
                    placeholder="Confirm Password"
                    type="password"
                    class="form-control"
                    v-model="user.passwd2"
                    id="password2"
                    required
                    />
            </div>
          <button class="submitForm">Register</button>
          <router-link class="registerbtn" :to="{ name: 'login' }">
            Already have an account?
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
    fetchUserData: function () {

    },
    adduser: function () {
      // Validation
      this.$http.get('http://localhost:5000/listUsers').then(
        (response) => {
          var users = response.body
          if (users.length !== 0) {
            for (let i = 0; i < users.length; i++) {
              if (users[i].email === this.user.email) {
                console.log('User already registered')
                return false
              }
            }
            var passwd = this.user.passwd
            var passwd2 = this.user.passwd2

            if (passwd !== passwd2) {
              alert('Passwords must be the same')
              return false
            } else {
              this.user.passwd = this.user.passwd
            }
            this.$http
              .post('http://localhost:5000/createUser', this.user, {
                headers: {
                  'Content-Type': 'application/json'
                }
              })
              .then(
                (response) => {
                  alert(response.body['mensagem'])
                  localStorage.setItem('user_info', JSON.stringify({'name': this.user.name, 'email': this.user.email, 'passwd': this.user.passwd}))
                  this.user = {}
                  this.$router.push('list')
                },
                (response) => {
                  alert(response.body['mensagem'])
                }
              )
            this.$http
              .post('http://localhost:5000/createUser', this.user, {
                headers: {
                  'Content-Type': 'application/json'
                }
              })
              .then(
                (response) => {
                  this.user = {}
                  alert(response.body['mensagem'])
                  this.$router.push('list')
                },
                (response) => {
                  alert(response.body['mensagem'])
                }
              )
          }
        },
        (response) => {}
      )
    }
  }
}
</script>
