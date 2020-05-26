<template>
    <div class="">
        <h2>User Registration</h2>
        <form id="formvideo" @submit.prevent="CreateUser">
            <p>
                <label for="username">Username:</label>
                <input class="ml2" type="text" name="username" id="username" v-model="username">
            </p>
            <p>
                <label for="password">Password:</label>
                <input class="ml2" type="password" name="password" id="password" v-model="password">
            </p>
            <p class="ml-4">
                <label for="email">Email:</label>
                <input type="text" name="email" id="email" v-model="email">
            </p>
            <p>
                <input class='btn btn-primary' type="submit" value="Register">
            </p>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    export default {
        name: "Register.vue",
        data() {
            return {
                username: null,
                password: null,
                email: null
            }
        },
        methods: {
            CreateUser() {
                console.log(this.username)
                console.log(this.password)
                axios.post('http://127.0.0.1:8000/api/users/', {
                    username: this.username,
                    password: this.password,
                    email: this.email,
                })
                .then(res => console.log(res))
                .catch(err => console.log(err));
                this.$router.push('/')
            }
        }

    }
</script>

<style scoped>

</style>