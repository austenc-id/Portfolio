<template>
  <LoadScreen v-if="active.loadScreen" :message="loading.message" :time="loading.time" />
  <main v-else class="app">
    <Header :titles="header.titles" :links="header.links" />
    <Navbar :chapters="chapters" />

  </main>

</template>

<script>
import LoadScreen from './components/LoadScreen.vue'
import Header from './components/Header'
import Navbar from './components/Navbar'
import { collector } from './scripts/Fetch'
import { utils } from './scripts/utils'
export default {
  name: 'App',
  components: {
    LoadScreen,
    Header,
    Navbar,
  },
  created() {
    this.loadContent()
  },
  mounted() { },
  data() {
    return {
      urls: {
        base: 'https://acmf-dev.herokuapp.com/api',
      },
      active: {
        loadScreen: true,
      },
      loading: {
        message: "Waking up Heroku Dyno...",
        time: "(may take up to 10 seconds)",
      },
      header: {
        titles: {
          title: 'Austen Myers',
          subTitle: 'Demo',
        },

        links: [],
      },
      chapters: [],
    }
  },
  methods: {
    async loadContent() {
      await collector.fetchContent(this.urls.base)
        .then(data => {
          this.loading.message = 'Collecting Data...'
          this.loading.time = 5
          this.header.links = data.links
          this.chapters = data.chapters;
          this.countdown()
        })
    },
    async countdown() {
      while (this.loading.time > 0) {
        await utils.sleep(1)
          .then(data => {
            this.loading.time--
            console.log(this.loading.time)
            if (this.loading.time === 0) {
              this.active.loadScreen = false
            }
          })
          .catch(error => console.log(error))
      }
    }
  }
}
</script>

<style>
@import './assets/style/style.css';
</style>
