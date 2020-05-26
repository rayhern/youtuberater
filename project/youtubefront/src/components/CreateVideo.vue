<template>
  <div class="">
    <div class="row">
        <div class="col-md-4 mx-auto py-auto">
            <h2>Create new video</h2>
            <p v-if="errors.length">
                <b>Please correct the following error(s):</b>
                <ul>
                    <li v-for="error in errors"><span v-html="error"></span></li>
                </ul>
            </p>
            <div class="card">
                <div class="card-body from-group">
                    <form id="formvideo" @submit.prevent="checkForm">
                        <p>
                            <label for="title">Title:</label>
                            <input class="form-control" type="text" id="title" name="title" v-model="title">
                        </p>
                        <p>
                            <label for="description">Description:</label>
                            <input class="form-control" type="textarea" id="description" name="title" v-model="description">
                        </p>
                        <p>
                            <label for="url">URL:</label>
                            <input class="form-control" type="text" id="url" name="title" v-model="url">
                        </p>
                        <p>
                            <label for="category">Category:</label>
                            <select class="form-control" id="category" name="category" v-model="category">
                                <option>web_development</option>
                                <option>programming</option>
                                <option>music</option>
                            </select>
                        </p>
                        <p>
                            <label for="subcategory">Subcategory:</label>
                            <input class="form-control" type="text" id="subcategory" name="subcategory" v-model="subcategory">
                        </p>
                        <p>
                            <label for="author">Author:</label>
                            <input class="form-control" type="text" id="author" name="author" v-model="author">
                        </p>
                        <p>
                            <input class="btn-sm btn-primary" type="submit" value="Create Video" @click="$emit('createdvideo')">
                        </p>
                    </form>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

export default {
  name: 'CreateVideo.vue',
    components: {

    },
    data() {
      return {
          title: null,
          description: null,
          url: null,
          category: null,
          subcategory: null,
          author: null,
          errors: [],
      }
    },
    methods: {
      checkForm() {
          this.errors = [];
          axios.post('http://127.0.0.1:8000/api/videos/', {
              title: this.title,
              description: this.description,
              url: this.url,
              category: this.category,
              subcategory: this.subcategory,
              author: this.author
          })
          .then(res => {
              console.log(res)
              this.$router.push('/')
          })
          .catch(err => {
              console.log(err)
              for(let the_error in err.response.data) {
                  this.errors.push('<b>' + the_error + '</b>' + ' - ' + err.response.data[the_error][0])
              }
          })
      }
    }
}
</script>
