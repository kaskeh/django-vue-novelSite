<template>
  <div class="header">
    <b-container>
      <!-- 使用b-container进行包裹，使得原先占满整个宽度的情况，变得左右均有一定的距离-->
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">可容书阁</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item
              v-for="item in headData.headers"
              :key="item.id"
              :href="item.url"
            >
              {{ item.text }}
            </b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input
                size="sm"
                class="mr-sm-2"
                placeholder="输入小说名字或者作者名称"
              >
              </b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit"
                >查询
              </b-button>
            </b-nav-form>

            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template #button-content>
                <em>用户中心</em>
              </template>
              <b-dropdown-item href="/homeUser" v-show="showUserName">
                {{ username }}，欢迎回来！
              </b-dropdown-item>
              <b-dropdown-item href="/login" v-show="!showUserName">
                登录
              </b-dropdown-item>
              <b-dropdown-item :href="logInOn">
                {{ logInOnInfo }}
              </b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </b-container>
  </div>
</template>

<script>
import { reactive } from "vue";
import { GetCates } from "../../apis/read.js";
export default {
  name: "pageHeader",
  data() {
    return {
      logInOn: "register",
      logInOnInfo: "注册用户",
      showUserName: false,
      username: "",
    };
  },
  // setup生命周期函数，较beforeCreate与created先前调用
  setup() {
    const headData = reactive({
      headers: [],
    });
    GetCates().then(
      (response) =>
        // console.log(response),
        (headData.headers = response.data.data)
    );
    return {
      headData,
    };
  },
  mounted() {
    // 查看缓存中是否有用户的名称
    let user = localStorage.user_name;
    if (user != undefined) {
      console.log("用户信息存在");
      this.username = user;
      this.logInOn = "logOut";
      this.logInOnInfo = "注销用户";
      this.showUserName = true;
      return;
    }
    this.username = user;
    this.logInOn = "register";
    this.logInOnInfo = "注册用户";
    this.showUserName = false;
    // console.log("用户信息存在");
  },
  methods: {
    userLogOut() {
      console.log("用户退出");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
#nav-collapse {
  /* 由于使用了bootstrap-vue-3，使得原先的导航栏中容器中的项目的主轴排序使用了默认的左对齐
  而导致外观上的不和谐，故使用space-around的两端对齐 */
  justify-content: space-between;
}
</style>
