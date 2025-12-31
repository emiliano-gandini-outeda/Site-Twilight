import { createApp } from "vue"
import "./style.css"
import App from "./App.vue"
import router from "./router"
import Header from './components/Header.vue'
import Footer from "./components/Footer.vue"
import Personajes from "./components/Personajes.vue"

createApp(App)
  .use(router)
  .mount("#app")
  .component("Header", Header)
  .component("Footer", Footer)
  .component("Personajes", Personajes)
