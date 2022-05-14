<template>
  <LoadScreen v-if="active.loadScreen" />
  <main v-else class="app">
    <Header v-if="active.header" />
    <Navbar v-if="active.navbar" />
  </main>
</template>

<script>
import LoadScreen from "./components/LoadScreen.vue";
import Header from "./components/Header";
import Navbar from "./components/Navbar";
export default {
  name: "Index",
  components: {
    LoadScreen,
    Header,
    Navbar,
  },
  created() {
    this.loadContent();
  },
  mounted() {},
  data() {
    return this.$store.state;
  },
  methods: {
    async loadContent() {
      await this.$store.dispatch("fetchLinks");
      await this.$store.dispatch("fetchChapters");
      this.loading.message = "Collecting Data...";
      this.loading.time = 5;
      this.countdown();
    },
    async countdown() {
      while (this.loading.time > 0) {
        await this.sleep(1)
          .then((data) => {
            this.loading.time--;
            if (this.loading.time === 0) {
              this.active.loadScreen = false;
              this.active.header = true;
              this.active.navbar = true;
            }
          })
          .catch((error) => console.log(error));
      }
    },
    sleep(sec) {
        let ms = sec * 1000
        return new Promise(resolve => setTimeout(resolve, ms));
    }
  },
};
</script>

<style>
@import "./assets/style/style.css";
</style>
