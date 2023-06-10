<template>
  <div id='delete-recipe'>
    <h2>Delete a recipe</h2>
    <form v-on:submit.prevent='deleterecipe'>
      <div class="form-group">
        <label name="recipe_title">Title: </label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.title"
          id="recipe_title"
          disabled
        />
      </div>
      <div class="form-group">
        <label name="recipe_autor">Autor: </label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.autor"
          id="recipe_autor"
          disabled
        />
      </div>
      <div class="form-group">
        <label name="recipe_ingredients">Ingredients:</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.ingredients"
          id="recipe_ingredients"
          disabled
        />
      </div>
      <div class="form-group">
        <label name="recipe_how">How to:</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.how"
          id="recipe_how"
          disabled
        />
      </div>
      <div class="form-group">
        <label name="recipe_image">Image URL</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.image"
          id="recipe_image"
          disabled
        />
      </div>
      <div class="form-group">
        <label name="recipe_time">Prep time (min)</label>
        <input
          type="number"
          class="form-control"
          v-model="recipe.time"
          id="recipe_time"
          disabled
        />
      </div>
      <div class='form-group'>
        <button class='btn btn-primary'>Delete</button>
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
  created: function () {
    this.getrecipeData()
  },
  methods: {
    getrecipeData: function () {
      this.$http
        .get('http://localhost:5000/getid/' + this.$route.params.id)
        .then(
          (response) => {
            this.recipe.id = this.$route.params.id
            this.recipe.title = response.body['title']
            this.recipe.autor = response.body['autor']
            this.recipe.ingredients = response.body['ingredients']
            this.recipe.how = response.body['how']
            this.recipe.image = response.body['image']
            this.recipe.time = response.body['time']

            this.$forceUpdate()
          },
          (response) => {}
        )
    },
    deleterecipe: function () {
      this.$http.get('http://localhost:5000/delete/' + this.recipe.id).then(
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
