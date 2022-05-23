import { defineNuxtConfig } from "nuxt";

// https://v3.nuxtjs.org/api/configuration/nuxt.config
// export default defineNuxtConfig({});

export default defineNuxtConfig({
  build: {
    postcss: {
      postcssOptions: {
        plugins: {
          tailwindcss: {},
          autoprefixer: {},
        },
      },
    },
  },
  generate: {
    routes: ["/login"],
  },
  css: ["~/assets/css/tailwind.css"],

  publicRuntimeConfig: {
    axios: {
      baseURL: "https://api.covidtracking.com/",
    },
  },

  modules: [["@nuxtjs/axios", { proxyHeaders: false }], "@nuxtjs/proxy"],
});
