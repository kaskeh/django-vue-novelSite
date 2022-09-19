<template>
  <div class="home">
    <homeHeader />
    <homeBody />
    <homeFooter />
  </div>
</template>

<script>
// @ is an alias to /src
import homeHeader from "@/components/siteHeaders/headerStyle0.vue";
import homeBody from "@/components/siteBodys/bodyStyle0.vue";
import homeFooter from "@/components/siteFooters/footerStyle0.vue";

export default {
  name: "HomeView",
  components: {
    homeHeader,
    homeBody,
    homeFooter,
  },
};
</script>
