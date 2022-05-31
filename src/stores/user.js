import { defineStore } from "pinia";
import http from "../http-common";

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
      this.authenticated = true;
      this.desc = inf;
    },
    logout() {
      this.authenticated = false;
      this.desc = {
        author: false,
        email: "",
        firstName: "",
        isActive: false,
        lastName: "",
        username: "",
      };
      http
        .post("/users/", {
          query: `
          mutation{
            deleteTokenCookie{
              deleted
            }
          }
        `,
        })
        .then((response) => {})
        .catch((err) => {
          console.log(err);
        });
    },
  },
});
