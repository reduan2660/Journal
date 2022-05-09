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
});
