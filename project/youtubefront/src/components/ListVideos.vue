<template>
    <div class="">
        <div class="row">
            <div class="col-md-5 text-center nicefont">
                <h4>Welcome to Youtube Rater</h4>
                    <b-button :to="{name: 'CreateVideo'}" size="sm" class="my-2 center" type="submit" variant="primary">Create Video</b-button>

<!--                <form @submit="createdNew()">-->
<!--                    <input class="btn-sm btn-primary mb-3 btn-center" id="createdNew" type="submit" value="Create New Video">-->
<!--                </form>-->
                <p v-bind:key="video.id" v-for="video in videos">
                    {{video.title}}
                    <br>
                    Rating: {{video.rating_average}}
                    <br>
                    <button class="btn-sm btn-primary mt-2 mt-3" v-on:click="videoDetail(video)">Details</button>
                </p>
            </div>
            <div class="col-md-6">
                <VideoDetails v-bind:videodetail="videodetail" v-on:updated="getVideos" v-on:deleted="updateVideos"></VideoDetails>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import VideoDetails from "./VideoDetails";
    import CreateVideo from "./CreateVideo";

    export default {
        name: "ListVideos",
        components: {
            VideoDetails,
            CreateVideo,
        },
        data() {
            return{
                videos: [],
                videodetail: Object,
            }
        },
        methods: {
            getVideos() {
                console.log('get videos');
                axios.get('http://127.0.0.1:8000/api/videos/')
                .then(res => (this.videos = res.data))
                .catch(err => console.log(err));
            },
            videoDetail(video) {
                this.videodetail = video;
            },
            updateVideos(video) {
                this.timer = setTimeout(() => {
                    axios.get('http://127.0.0.1:8000/api/videos/')
                    .then(res => (this.videos = res.data))
                    .catch(err => console.log(err));
                }, 600);

            }
        },
        created() {
            this.getVideos()
        }
    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Alatsi&display=swap');

    .nicefont{
        font-size:20px;
        font-family: 'Alatsi', 'sans-serif';
    }
</style>