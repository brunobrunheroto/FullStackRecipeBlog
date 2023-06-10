<template>
  <div id="update-recipe">
    <h2>Update a recipe</h2>
    <form v-on:submit.prevent="updaterecipe">
      <div class="form-group">
        <label name="recipe_title">Title</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.title"
          id="recipe_title"
          required
        />
      </div>

      <div class="form-group">
        <label name="recipe_autor">Autor</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.autor"
          id="recipe_autor"
          required
        />
      </div>

      <div class="form-group">
        <label name="recipe_ingredients">ingredients</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.ingredients"
          id="recipe_ingredients"
          required
        />
      </div>

      <div class="form-group">
        <label name="recipe_how">How to</label>
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
        <label name="recipe_time">Prep time</label>
        <input
          type="text"
          class="form-control"
          v-model="recipe.time"
          id="recipe_time"
          required
        />
      </div>

      <div class="form-group">
        <button class="btn btn-primary">Update</button>
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
      this.$http.get('http://localhost:5000/getid/' + this.$route.params.id).then(
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
    updaterecipe: function () {
      // Validation
      var time = parseFloat(this.recipe.time)
      if (isNaN(time)) {
        alert('Prep time must be a number')
        return false
      } else {
        this.recipe.time = this.recipe.time
      }
      this.$http
        .post('http://localhost:5000/update', this.recipe, {
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
