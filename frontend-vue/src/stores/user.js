import { defineStore } from "pinia";

export const useUserStore = defineStore({
  id: "user",
  state: () => ({
    authenticated: false,
    desc: {
      author: false,
      email: "",
      firstName: "",
      isActive: false,
      lastName: "",
      username: "",
    },
  }),
  getters: {
    isAuthenticated: (state) => state.authenticated,
    info: (state) => state.desc,
  },
  actions: {
    authenticate(inf) {
      this.desc = inf;
    },
  },
});
