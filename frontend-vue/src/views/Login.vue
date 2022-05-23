<template>
  <div
    class="min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0"
  >
    <div class="text-h2 text-4xl">Journal</div>

    <div class="w-full sm:max-w-md mt-6 px-6 py-4 bg-white overflow-hidden">
      <form method="POST" action="#" data-bitwarden-watching="1">
        <!-- <input type="hidden" name="_token" :value="csrf" /> -->
        <div>
          <label class="block font-medium text-base" for="email"> Email </label>
          <input
            class="border-black border-2 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 rounded-md shadow-sm block w-full mt-1 py-2 indent-2"
            id="email"
            type="email"
            name="email"
            required
            autofocus
            v-model="loginInfo.email"
          />
        </div>

        <div class="mt-4">
          <label class="block font-medium text-base" for="password">
            Password
          </label>
          <input
            class="border-black border-2 focus:ring focus:ring-indigo-200 focus:ring-opacity-50 rounded-md shadow-sm block w-full mt-1 py-2 indent-2"
            id="password"
            type="password"
            name="password"
            required
            v-model="loginInfo.password"
          />
        </div>

        <div class="mt-4 flex flex-row justify-between items-center">
          <label for="remember_me" class="flex items-center">
            <input
              type="checkbox"
              class="rounded border-gray-300 text-black shadow-sm focus:border-gray-500 focus:ring focus:ring-gray-200 focus:ring-opacity-50"
              id="remember_me"
              name="remember"
              v-model="loginInfo.remember"
            />
            <span class="ml-2 text-sm">Remember me</span>
          </label>

          <div class="block">
            <span class="ml-2 text-sm">{{ ui.feedback.value }}</span>
          </div>
        </div>

        <div class="flex items-center justify-end mt-4 space-x-4">
          <a class="text-gray" href="#">
            <span> Forgot your password? </span>
          </a>

          <Btn @click.prevent="login"> {{ ui.loginBtnText.value }} </Btn>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { reactive } from "@vue/reactivity";
import http from "../http-common";
import { useUserStore } from "../stores/user";

export default {
  setup() {
    const ui = reactive({
      loginBtnText: {
        value: "Log in",
        loading: "Logging in",
        default: "Log in",
        success: "Logged in",
        failed: "Log in Failed",
      },
      feedback: {
        value: "",
        default: "",
        loginFailed: "Check you information again.",
        loginError: "Error Occured. Try again later.",
      },
    });

    const user = useUserStore();

    const loginInfo = reactive({
      email: "alve@gmail.com",
      password: "asdfgh233",
      remember: false,
    });

    function login() {
      ui.loginBtnText.value = ui.loginBtnText.loading;
      http
        .post("/users/me", {
          query: `
          mutation {
            tokenAuth(
              email: "${loginInfo.email}"
              password: "${loginInfo.password}"
            ) {
              success,
              errors,
              token,
              refreshToken,
              user {
                username,
                firstName,
                lastName,
                email,
                isActive,
                author
              }
            }
          }
        `,
        })
        .then((response) => {
          if (!!response.data.data.tokenAuth) {
            // Store Update
            user.authenticate(response.data.data.tokenAuth.user);

            // Ui Update
            ui.loginBtnText.value = ui.loginBtnText.success;
            ui.feedback.value = ui.feedback.default;

            console.log(user.info);
          } else {
            // Ui Update
            ui.loginBtnText.value = ui.loginBtnText.failed;
            ui.feedback.value = ui.feedback.loginFailed;
          }
        })
        .catch((error) => {
          ui.feedback.value = ui.feedback.loginError;
          console.log(error);
        });
    }

    return {
      ui,
      user,
      loginInfo,
      login,
    };
  },
};
</script>
