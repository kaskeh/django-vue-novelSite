<template>
  <div id="bg">
    <div id="container">
      <h1>个人信息</h1>
      <p><span>账号：</span>{{ sname }}</p>
      <p><span>邮箱:</span>{{ smail }}</p>
      <p><span>手机号：</span>{{ stel }}</p>
      <button @click.prevent="comeIndex">返回主页</button>
      <button @click.prevent="logout">退出</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "userHome",
  data() {
    return {
      //获取用户信息到主页
      sname: localStorage.getItem("username"),
      smail: localStorage.getItem("mail"),
      stel: localStorage.getItem("tel"),
    };
  },
  methods: {
    comeIndex: function () {
      this.$router.replace("/"); //页面跳转至站点主页面
    },
    //当点击退出按钮，将不保存登录状态
    logout: function () {
      this.$router.replace("/login"); //页面跳转至登录页面
      window.localStorage.clear();
      window.document.cookie.clear();

      // 发送一个通知到服务端，告知该用户退出了
    },
  },
  mounted() {
    if (!localStorage.getItem("username")) {
      console.log("当前用户信息不存在");
      this.$router.replace("/login"); //页面跳转至登录页面
    }
  },
};
</script>

//css
<style scoped>
#container {
  width: 480px;
  height: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #00000090;
  text-align: center;
  border-radius: 20px;
  margin-top: 10px;
  color: white;
}
#bg {
  width: 100%;
  height: 100%;
  /* background: url("../assets/bg2.jpg"); */
  background-color: blueviolet;
  background-size: 100% 100%;
  position: fixed;
  top: 0;
  left: 0;
}
p {
  font-size: 20px;
  margin-top: 20px;
  text-align: left;
  margin-left: 32%;
}
button {
  position: relative;
  height: 33px;
  width: 150px;
  background: rgba(35, 19, 252, 0.425);
  border-radius: 10px;
  margin-top: 10px;
  box-shadow: none;
  color: white;
  margin-left: 10px;
}
</style>
