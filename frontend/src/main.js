import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import BootstrapVue from "bootstrap-vue-3";

import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue-3/dist/bootstrap-vue-3.css";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";

createApp(App)
  .use(ElementPlus)
  .use(BootstrapVue)
  .use(store)
  .use(router)
  .mount("#app");
