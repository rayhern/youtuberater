<template>
    <div class="main-text" v-if="videodetail.title != null">
        <div class="row">
            <div class="col-md-10" v-bind.sync="videodetail">
                <p class="mb-3"><span class="bodyp">Title: </span>{{videodetail.title}}</p>
                <iframe width="450" height="260" :src="videodetail.url" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                <p><span class="bodyp">Description: </span>{{videodetail.description}}</p>
                <p><span class="bodyp">Rating: </span>{{videodetail.rating_average}}</p>
                <p><span class="bodyp">Category: </span>{{videodetail.category}}</p>
                <p v-if="videodetail.comments_list.length > 0"><span class="bodyp">Comments: </span></p>
                <div class="card" v-if="videodetail.comments_list.length > 0">
                    <div class="card-body">
                        <p v-if="videodetail.comments_list.length > 0" v-for="comment in videodetail.comments_list"><span v-html="comment"></span></p>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div class="card col-md-10">
            <div class="card-body centered">
                <form id="formvideo" class="form-group" @submit.prevent="giveRating">
                    <p>
                        <label for="stars">Stars</label>
                        <input class="form-control ml-auto mr-auto" id="stars" type="text" name="stars" v-model="stars">
                    </p>
                    <p>
                        <label for="comments">Comments</label>
                        <textarea class="form-control ml-auto mr-auto" id="comments" name="comments" v-model="comments"></textarea>
                    </p>
                    <p>
                        <input class="btn-primary form-control" type="submit" value="Submit Rating">
                    </p>
                </form>
            </div>
        </div>
        <div class="col-md-10 pt-3 pb-3">
            <button class="btn-sm btn-danger" v-on:click="videoDelete(videodetail)" @click="$emit('deleted', videodetail)">Delete Video</button>
        </div>
    </div>
    <div class="main-text" v-else>
        Here you will find my dank videos that you can rate. Please be respectful in the comments. Peace and love.
    </div>
</template>

<script>
    import axios from 'axios';
    import {TokenService} from "../storage/service";

    export default {
        name: "VideoDetails",
        props: {
            videodetail: {}
        },
        data() {
            return{
                stars: "",
                comments: "",
            }
        },
        methods: {
            videoDelete(videodetail) {
                console.log(this.token);
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.delete('http://127.0.0.1:8000/api/videos/' + this.videodetail.id, axiosConfig)
                .then(res => {
                    console.log(res.data);
                    this.timer = setTimeout(() => {
                        this.videodetail = {};
                    }, 600);
                })
                .catch(res => console.log(res.data))
            },
            giveRating(stars, comments) {
                this.token = TokenService.getToken()
                if (parseInt(this.stars) > 5) {
                    alert('You cannot rate a video with more than 5 stars.');
                    this.stars = ''
                    this.comments = ''
                    return;
                }
                if (parseInt(this.stars) < 0) {
                    alert('You cannot rate a video with less than 1 star.');
                    this.stars = ''
                    this.comments = ''
                    return;
                }
                let postData = {
                    stars: this.stars,
                    comments: this.comments
                }
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                };
                axios.post('http://127.0.0.1:8000/api/videos/' + this.videodetail.id + '/rate_video/', postData, axiosConfig)
                .then(res => {
                    console.log(res.data)
                    this.$emit('updated')

                    axios.get('http://127.0.0.1:8000/api/videos/' + this.videodetail.id, axiosConfig)
                    .then(res => this.videodetail=res.data)

                    this.stars = ''
                    this.comments = ''

                })
                .catch(res => console.log(res.data))
            }
        },
        created() {
            this.token = TokenService.getToken() || null;
        }
    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Muli&display=swap');
    .main-text {
        font-family: 'Muli', sans-serif;
        font-size: 20px;
        color: black,
    }
    .bodyp {
        color: blue;
        font-family: 'Muli', sans-serif;
        font-size: 20px;
    }
</style>