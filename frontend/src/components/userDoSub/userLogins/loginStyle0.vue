<template>
  <div id="background">
    <div class="container">
      <form action="">
        <h1>登录</h1>
        <div class="form">
          <div class="item">
            <label>用户名：</label>
            <input
              type="text"
              name="username"
              v-model.trim="name"
              placeholder="请输入用户名"
            />
            <!-- v-model把输入的值传输给name变量 -->
            <br />
          </div>
          <div class="item">
            <label>密码：</label>
            <!-- v-model.trim 将用户输入的前后的空格去掉 -->
            <input
              type="password"
              name="password"
              v-model.trim="password"
              placeholder="请输入密码"
            />
            <br />
          </div>
          <!-- <div class="keep">
            <input
              @click="handlesave"
              id="yes"
              type="radio"
              value="0"
            />// 点击选中
            <label for="yes">保持登录状态</label>
          </div> -->
        </div>
      </form>
      <button type="submit" @click.prevent="login_ButtonCheck">登录</button>
      <!-- v-on点击按钮触发handlelogin方法 -->
      <button @click.prevent="handleregister">注册</button>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
// import { thisExpression } from '@babel/types';
import instance from "@/utils/login_request";
export default {
  data() {
    return {
      name: "", //姓名，用v-model绑定监听，将输入的字符串赋值给name变量
      password: "", //密码
    };
  },
  methods: {
    //点击【登录】后用自定义的instance方法发送axios请求
    login_ButtonCheck: function () {
      console.log("点击登录了");
      let usr_val = this.name;
      let pwd_val = this.password;
      // console.log("开始登录");
      //自定义的instance方法向后端发起post请求，常规axios写法为 this.axios.post
      instance
        .post("/user/login/", {
          username: usr_val,
          password: pwd_val,
        })
        .then((res) => {
          //登录成功
          //用this.$store.commit调用上面store/index.js文件中vuex里自定义的mSetTokenInfo方法保存登录成功返回的token
          //res.data.access是返回信息中token所在的字段名，如不知道请回顾上面Django中自定义返回信息里定义的token返回字段
          this.$store.commit("mSetTokenInfo", res.data.data.access);
          // console.log("用户的tokne", res.data.data.access);
          //登录成功后跳转Home页并将用户信息传至Home页
          this.$router.push({
            name: "userHome",
            param: {
              username: res.data.data.username,
              department: res.data.data.user_type,
            },
          });
          // 刷新下用户名称
          localStorage.setItem("username", res.data.user_name);
          console.log("登录成功", res);
        })
        .catch((error) => {
          //登录失败
          console.log("登录失败", error);
        });
    },
    // handlelogin: function () {
    //   if (
    //     // this.name === localStorage["name"] &&
    //     // this.password === localStorage["password"]
    //     this.name &&
    //     this.password
    //   ) {
    //     this.$router.push("/userHome"); //如果输入的名字以及密码正确路由跳转至个人页面
    //   } else if (this.name === "") {
    //     //名字为空
    //     alert("用户名不为空");
    //   } else if (this.password === "") {
    //     //密码为空
    //     alert("密码不为空");
    //   } else {
    //     alert("账号不存在，请注册后登录"); //查无此号
    //     // console.log(this.name, this.password);
    //   }
    // },
    handleregister: function () {
      this.$router.push("/register"); //点击注册按钮，跳转至注册页面
    },
    // //点击保持登录状态触发handlesave
    // handlesave: function () {
    //   this.st = "true"; //修改登录状态为true
    //   localStorage.setItem("s", this.st);
    //   console.log(localStorage.s);
    // },
  },
};
</script>

<style scoped>
#background {
  width: 100%;
  height: 100%;
  /* background: url("../assets/bg2.jpg"); */
  background-color: #4e5ef3;
  background-size: 100% 100%;
  position: fixed;
  top: 0;
  left: 0;
}
.container {
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
}
.container h1 {
  color: aliceblue;
  margin-left: 20px;
}
.item {
  color: white;
  margin-left: 15%;
  margin-top: 35px;
  font-size: 20px;
  text-align: left;
}
.item label {
  float: left;
  width: 5em;
  margin-right: 1em;
  text-align: right;
}
input {
  margin-left: -5px;
  padding: 4px;
  border: solid 1px #4e5ef3;
  outline: 0;
  font: normal 13px/100% Verdana, Tahoma, sans-serif;
  width: 200px;
  height: 23px;
  background: #f1f1f190;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 8px;
}
button {
  position: relative;
  height: 33px;
  width: 100px;
  background: rgba(35, 19, 252, 0.425);
  border-radius: 10px;
  margin-top: 18px;
  box-shadow: none;
  color: white;
  margin-left: 40px;
  margin-right: 10px;
}
.keep {
  color: white;
}
.keep input {
  width: 15px;
  height: 15px;
  margin-top: 7px;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
