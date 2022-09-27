<template>
  <div class="logout">
    <p>您已退出</p>
  </div>
</template>
<script>
import { onMounted } from "vue";
export default {
  setup() {
    onMounted(() => {
      localStorage.removeItem("user_token");
      localStorage.removeItem("user_id");
      localStorage.removeItem("user_name");

      sessionStorage.removeItem("user_token");
      sessionStorage.removeItem("user_id");
      sessionStorage.removeItem("user_name");
    });
  },
};
</script>
