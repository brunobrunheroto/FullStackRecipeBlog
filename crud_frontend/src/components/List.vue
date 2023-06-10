<template>
  <div id="list-recipes">
    <h2>See the latest recipes</h2>
    <div class="recipe" v-for='recipe in recipes' v-bind:key='recipe'>
        <img width=auto height=auto :src="recipe.image"/>
        <div class="column">
          <h4>{{ recipe.title }}</h4>
          <p>Written by: {{ recipe.autor }}</p>
          <p>Ingredients: {{ recipe.ingredients }}</p>
          <p>How to: {{ recipe.how }}</p>
          <p>Prep Time (min): {{ recipe.time }}</p>
          <div>
          <router-link
              :to="{ name: 'update', params: { id: recipe._id['$oid'] } }"
              class="btn btn-primary"
              >Update recipe</router-link
            >
            <router-link
              :to="{ name: 'delete', params: { id: recipe._id['$oid'] } }"
              class="btn btn-danger"
              >Delete recipe</router-link
            >
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      recipes: []
    }
  },

  created: function () {
    this.fetchrecipeData()
  },

  methods: {
    fetchrecipeData: function () {
      this.$http.get('http://localhost:5000/index').then(
        (response) => {
          this.recipes = response.body
        },
        (response) => {}
      )
    }
  }
}
</script>
