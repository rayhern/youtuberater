<template>
    <div class="">
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand class="text-white" :to="{name: 'Home'}">Youtube Rater</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-navbar-nav class="ml-auto">
                <b-nav-form @submit.prevent="login" v-if="token===null">
                    <b-form-input id="username" size="sm" class="mr-sm-2" v-model="username" placeholder="username" name="username"></b-form-input>
                    <b-form-input id="username" size="sm" class="mr-sm-2" v-model="password" placeholder="password" name="password" type="password"></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
                </b-nav-form>
                <b-nav-form @submit.prevent="logout" v-if="token !== null">
                    <b-button type="submit" size="sm" class="my-2 ml-2"> Logout</b-button>
                </b-nav-form>
                <b-nav-form @submit.prevent="register" v-if="token === null">
                    <b-button :to="{name: 'Register'}" type="submit" size="sm" class="my-2 ml-2">Register</b-button>
                </b-nav-form>

            </b-navbar-nav>
        </b-navbar>

    </div>

</template>

<script>

    import axios from 'axios'
    import {TokenService} from "../storage/service";

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"

    export default {
        name: "Header.vue",
        components: {

        },
        data() {
            return{
                username: '',
                password: '',
                token: localStorage.getItem('user-token') || null,
            }
        },
        methods: {
            login() {
                axios.post('http://127.0.0.1:8000/auth/', {
                    username: this.username,
                    password: this.password,
                })
                .then(resp => {
                    this.token = resp.data.token;
                    localStorage.setItem('user-token', this.token);
                })
                .catch(resp => {
                    localStorage.removeItem('user-token');
                })
            },
            logout() {
                this.username = '';
                this.password = '';
                localStorage.removeItem('user-token');
                this.token = null;
            },
            register() {
                console.log('router');
            }
        },
        created() {
            this.token = TokenService.getToken() || null;
        }
    }
</script>

<style scoped>

</style>