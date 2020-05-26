<template>
  <div class="home">
    <ListVideos/>
  </div>
</template>

<script>
// @ is an alias to /src
import ListVideos from "../components/ListVideos";

export default {
  name: 'Home',
  components: {
    ListVideos
  }
}
</script>
