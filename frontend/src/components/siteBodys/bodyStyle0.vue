<template>
  <div id="pageBody">
    <div>
      <lastUpdate />
    </div>
  </div>
</template>
<script>
import lastUpdate from "./bodyComps/newUpdateNovels.vue";
export default {
  components: {
    lastUpdate,
  },
};
</script>
<style scoped lang="scss">
// #pageBody {
//   background-color: aqua;
// }
</style>
