import { createApp } from "vue"
import "./style.css"
import App from "./App.vue"
import router from "./router"
import Header from './components/Header.vue'

createApp(App)
  .use(router)
  .mount("#app")
  .component("Header", Header)
