import { createApp } from "vue";
import { createStore } from "vuex";
import Index from "./Index.vue";
import { Production, Development } from "./store.js"

// const store = createStore(Production)
const store = createStore(Development)
const app = createApp(Index)

app.use(store)
app.mount("#app");
