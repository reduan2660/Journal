<template>
  <div class="underline">Hello : {{ user.isAuthenticated }}</div>
</template>

<script>
import { defineComponent } from "vue";
import { useUserStore } from "../stores/user";

export default {
  setup() {
    const user = useUserStore();

    return {
      user,
    };
  },
};
</script>
