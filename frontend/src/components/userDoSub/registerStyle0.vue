<template>
  <div id="background">
    <div id="contain">
      <h1>账号注册</h1>

      <div class="form">
        <label>用户名：</label>
        <input type="text" v-model.trim="name" autocomplete="off" /><br />
      </div>
      <div class="form">
        <form>
          <label>密码：</label>
          <input
            type="password"
            v-model.trim="password"
            autocomplete="off"
          /><br />
        </form>
      </div>
      <div class="form">
        <label>邮箱：</label>
        <input type="email" v-model.trim="mail" autocomplete="off" /><br />
      </div>
      <!-- <div class="form">
        <label>手机号：</label>
        <input type="tel" v-model.trim="tel" /><br />
      </div> -->
      <button @click.prevent="handlefinish">提交</button>
    </div>
  </div>
</template>

<script>
import { registerFrom } from "@/apis/read.js";
import { formToken } from "@/apis/read.js";
import axios from "axios";
import data from "bootstrap/js/dist/dom/data";
import Qs from "qs";
export default {
  name: "registerComp",
  props: {
    msg: String,
  },
  data() {
    return {
      name: "",
      password: "",
      mail: "",
      submitToken: "",
    };
  },
  methods: {
    //点击完成按钮触发handlefinish
    handlefinish: function () {
      // 当填写的用户名 密码 邮箱 内容不为空时，发送表单数据到服务端进行合规校验 重复校验
      if (this.name !== "" && this.password !== "" && this.mail !== "") {
        let data = {
          username: this.name,
          password: this.password,
          mail: this.mail,
        };
        registerFrom(data);
        localStorage.username = "11";
      } else if (this.name === "") {
        alert("用户名不能为空");
      } else if (this.password === "") {
        alert("密码不能为空");
      } else if (this.mail === "") {
        alert("邮箱不能为空");
      }
    },
  },
  mounted() {
    formToken().then(
      (response) => (
        (this.submitToken = response.data.token),
        // (this.submitToken = document.cookie.split("=")[1]),
        // console.log("submitToken", response.data.token),
        console.log("submitTokenCookies", this.submitToken)
      )
    );
  },
};
</script>

//css
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
#contain {
  width: 580px;
  height: 560px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #00000090;
  text-align: center;
  border-radius: 20px;
}
#contain h1 {
  color: white;
}
.form {
  color: white;
  margin-left: 20%;
  margin-top: 60px;
  font-size: 20px;
  text-align: left;
}
label {
  float: left;
  width: 5em;
  margin-right: 1em;
  text-align: right;
}
input,
textarea {
  margin-left: 10px;
  padding: 4px;
  border: solid 1px #4e5ef3;
  outline: 0;
  font: normal 13px/100% Verdana, Tahoma, sans-serif;
  width: 200px;
  height: 20px;
  background: #f1f1f190;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 0px 8px;
}
input:hover,
textarea:hover,
input:focus,
textarea:focus {
  border-color: #0d0aa1;
}
button {
  position: relative;
  height: 33px;
  width: 150px;
  background: rgba(35, 19, 252, 0.425);
  border-radius: 10px;
  margin-top: 38px;
  box-shadow: none;
  color: white;
  margin-left: 40px;
}
</style>
