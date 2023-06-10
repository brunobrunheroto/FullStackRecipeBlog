<template>
  <div id="create-recipe">
    <h2>Share a recipe</h2>
    <form v-on:submit.prevent="addrecipe">
      <div class="form-group">
        <label name="recipe_title">Title: </label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.title"
          id="recipe_title"
          required
        />
      </div>

      <div class="form-group">
        <label name="recipe_ingredients">Ingredients:</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.ingredients"
          id="recipe_ingredients"
          required
        />
      </div>
      <div class="form-group">
        <label name="recipe_how">How to:</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.how"
          id="recipe_how"
          required
        />
      </div>
      <div class="form-group">
        <label name="recipe_image">Image URL</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.image"
          id="recipe_image"
          required
        />
      </div>
      <div class="form-group">
        <label name="recipe_time">Prep time (min)</label>
        <input
          type="number"
          class="form-control"
          v-model="recipe.time"
          id="recipe_time"
          required
        />
      </div>

      <div class="form-group">
        <button class="btn btn-primary">Share</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      recipe: {}
    }
  },
  methods: {
    addrecipe: function () {
      let user = JSON.parse(localStorage.getItem('user_info'))
      if (user !== null) {
        this.recipe.autor = user['name']
      } else {
        this.recipe.autor = 'Anonymous'
      }
      // Validation
      var prepTime = parseFloat(this.recipe.time)
      if (isNaN(prepTime)) {
        alert('Preço deve ser um número')
        return false
      } else {
        this.recipe.time = this.recipe.time
      }
      this.$http
        .post('http://localhost:5000/create', this.recipe, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.recipe = {}
            alert(response.body['mensagem'])
            this.$router.push('list')
          },
          (response) => {
            alert(response.body['mensagem'])
          }
        )
    }
  }
}
</script>

<link rel="stylesheet" style="text/css" href="crud_frontend\static\style.css">
