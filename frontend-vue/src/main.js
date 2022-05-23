import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/tailwind.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);

// Components
import Btn from "./components/Btn.vue";
app.component("Btn", Btn);

app.mount("#app");
