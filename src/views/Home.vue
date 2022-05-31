<template>
  <div class="w-screen h-screen flex flex-col items-center justify-center">
    <template v-if="user.isAuthenticated">
      <pre
        >{{ user.info }}
      </pre>

      <Btn @click="user.logout">Log out</Btn>
    </template>

    <template v-else>
      <router-link to="login">
        <Btn>Login</Btn>
      </router-link>
    </template>
  </div>
</template>

<script>
import { useUserStore } from "../stores/user";
import Btn from "../components/Btn.vue";

export default {
  components: { Btn },
  computed: {
    user: () => {
      return useUserStore();
    },
  },
};
</script>
