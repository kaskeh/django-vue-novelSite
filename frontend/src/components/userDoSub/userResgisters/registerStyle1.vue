<template>
  <div class="login box">
    <img src="/static/image/Loginbg.3377d0c.jpg" alt="" />
    <!-- <img src="../../../../static/image/Loginbg.3377d0c.jpg" alt="" /> -->
    <div class="login">
      <div class="login-title">
        <img src="/static/image/Logotitle.1ba5466.png" alt="" />
        <!-- <img src="../../../../static/image/Logotitle.1ba5466.png" alt="" /> -->
        <!-- <p>帮助有志向的年轻人通过努力学习获得体面的工作和生活!</p> -->
      </div>
      <div class="login_box">
        <div class="title">
          <span
            :class="register_type == 0 ? 'current' : ''"
            @click="register_type = 0"
          >
            用户名/邮箱注册
          </span>
          <span
            :class="register_type == 1 ? 'current' : ''"
            @click="register_type = 1"
          >
            手机号注册
          </span>
        </div>
        <div class="inp" v-if="register_type == 0">
          <input
            v-model="username"
            type="text"
            placeholder="用户名 / 邮箱"
            class="user"
          />
          <input
            v-model="password0"
            type="password"
            name="pw0"
            class="pwd"
            placeholder="密码"
          />
          <input
            v-model="password1"
            type="password"
            name="pw1"
            class="pwd"
            placeholder="再次输入密码"
          />
          <div id="geetest1"></div>
          <button class="register_btn" @click="registerHandle">注册</button>
          <p class="go_login">
            已有账号
            <span>
              <router-link to="/login">立即登录</router-link>
            </span>
          </p>
        </div>
        <div class="inp" v-show="register_type == 1">
          <input
            v-model="mobile"
            @blur="checkMobileUnique"
            type="text"
            placeholder="手机号码"
            class="user"
          />
          <input
            v-model="password0"
            type="password"
            name="pw0"
            class="pwd"
            placeholder="密码"
          />
          <input
            v-model="password1"
            type="password"
            name="pw1"
            class="pwd"
            placeholder="再次输入密码"
          />
          <input
            v-model="sms_code"
            type="text"
            class="pwd"
            placeholder="短信验证码"
          />
          <button id="get_code">获取验证码</button>
          <button class="register_btn" @click="registerHandle">注册</button>

          <p class="go_login">
            已有账号
            <span>
              <router-link to="/login">立即登录</router-link>
            </span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import instance from "@/utils/login_request";
// import { tr } from "element-plus/es/locale";
export default {
  name: "registerComp",
  data() {
    return {
      register_type: 0,
      username: "",
      password0: "",
      password1: "", // 再次输入的密码
      mobile: "",
      sms_code: "", // 手机收到的短信验证码
    };
  },

  methods: {
    registerHandle() {
      // console.log("点击了登录");
      if (this.register_type == 0) {
        // console.log("当前使用了用户名/ 邮箱注册");
        if (this.checkPwd() == true && this.checkName == true) {
          console.log("注册校验都通过了");
        } else {
          let self = this;
          self.$alert(`注册失败，请检查输入是否规范`, `可容书阁`, {});
        }
      } else if (this.register_type == 1) {
        console.log("当前使用了手机号注册");
        if (this.checkMobile() == true && this.checkPwd() == true) {
          console.log("注册校验都通过了");
        } else {
          let self = this;
          self.$alert(`注册失败，请检查输入是否规范`, `可容书阁`, {});
        }
      }
      // // 登陆处理
      // instance
      //   .post("/login/", {
      //     username: this.username,
      //     password: this.password,
      //   })
      //   .then((res) => {})
      //   .catch((error) => {});
    },

    checkName() {
      // 设定用户名规则，验证输入的用户名是否符合规范
      // 规则：js正则表达 和python中正则表达式类似
      var re = /^[0-9a-zA-Z]\w{2,5}$/;
      var reE = /^[0-9a-zA-Z]{2,20}@[0-9a-zA-Z]{2,5}.[0-9a-zA-Z]{2,5}$/;
      // 验证输入的用户名是否符合规则
      // 如果不符合规则则提示：用户名不符合规范
      // 如果不指明状态一直都是underfined
      if (re.test(this.username) | reE.test(this.username)) {
        // 验证成功显示符合规范
        return true;
      } else {
        return false;
      }
    },
    checkPwd() {
      var re = /^[0-9a-zA-Z]{4,8}$/;
      if (
        re.test(this.password0) &&
        re.test(this.password1) &&
        this.password0 == this.password1
      ) {
        return true;
      } else {
        return false;
      }
    },
    checkMobile() {
      var re = /^1[3-9]\d{9}$/;
      if (re.test(this.mobile)) {
        return true;
      } else {
        return false;
      }
    },
    checkEmail() {},

    checkMobileUnique() {
      // 检查手机号的合法性[格式和是否已经被注册]
      console.log("用户输入手机号完成");
      instance
        .get(`/user/check_mobile/${this.mobile}`)
        .then((response) => {})
        .catch((error) => {
          this.$message.error("该手机号已被注册");
        });
    },

    //   get_geetest_capcha() {
    //     // 获取验证码
    //     this.$axios
    //       .get(`${this.$settings.Host}/users/geetest/`)
    //       .then((response) => {
    //         // 使用initGeetest接口
    //         // 参数1：配置参数
    //         // 参数2：回调，回调的第一个参数验证码对象，之后可以使用它做appendTo之类的事件
    //         let data = response.data;
    //         initGeetest(
    //           {
    //             gt: data.gt,
    //             challenge: data.challenge,
    //             product: "popup", // 产品形式，包括：float，embed，popup。注意只对PC版验证码有效
    //             offline: !data.success, // 表示用户后台检测极验服务器是否宕机，一般不需要关注
    //           },
    //           this.handlerPopup
    //         );
    //       })
    //       .catch((error) => {
    //         this.$message.error("获取验证码错误！");
    //       });
    //   },
    //   handlerPopup(captchaObj) {
    //     // 验证码的二次验证
    //     // 成功的回调
    //     let self = this;
    //     captchaObj.onSuccess(function () {
    //       var validate = captchaObj.getValidate();
    //       self.$axios
    //         .post(`${self.$settings.Host}/users/geetest/`, {
    //           geetest_challenge: validate.geetest_challenge,
    //           geetest_validate: validate.geetest_validate,
    //           geetest_seccode: validate.geetest_seccode,
    //         })
    //         .then((response) => {
    //           // 验证码验证通过，执行登录处理
    //           self.loginHandle();
    //         })
    //         .catch((error) => {
    //           self.$message.error("验证码验证错误！");
    //         });
    //     });
    //     // 将验证码加到id为captcha的元素里
    //     document.getElementById("geetest1").innerHTML = ""; // 先把原来容器中的验证码清空了，在添加新的验证码
    //     captchaObj.appendTo("#geetest1");
    //   },
  },
};
</script>

<style scoped>
.box {
  width: 100%;
  height: 100%;
  position: relative;
  overflow: hidden;
}
.box img {
  width: 100%;
  min-height: 100%;
}
.box .login {
  position: absolute;
  width: 500px;
  height: 400px;
  left: 0;
  margin: auto;
  right: 0;
  bottom: 0;
  top: -338px;
}
.login .login-title {
  width: 100%;
  text-align: center;
}
.login-title img {
  width: 190px;
  height: auto;
}
.login-title p {
  font-size: 18px;
  color: #fff;
  letter-spacing: 0.29px;
  padding-top: 10px;
  padding-bottom: 50px;
}
.login_box {
  width: 400px;
  height: auto;
  background: #fff;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.5);
  border-radius: 4px;
  margin: 0 auto;
  padding-bottom: 40px;
}
.login_box .title {
  font-size: 20px;
  color: #9b9b9b;
  letter-spacing: 0.32px;
  border-bottom: 1px solid #e6e6e6;
  display: flex;
  justify-content: space-around;
  padding: 50px 60px 0 60px;
  margin-bottom: 20px;
  cursor: pointer;
}
.login_box .title span.current {
  color: #4a4a4a;
  border-bottom: 2px solid #84cc39;
}

.inp {
  width: 350px;
  margin: 0 auto;
}
.inp input {
  outline: 0;
  width: 100%;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}
.inp input.user {
  margin-bottom: 16px;
}
.inp .rember {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  margin-top: 10px;
}
.inp .rember p:first-of-type {
  font-size: 12px;
  color: #4a4a4a;
  letter-spacing: 0.19px;
  margin-left: 22px;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  /*position: relative;*/
}
.inp .rember p:nth-of-type(2) {
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: 0.19px;
  cursor: pointer;
}

.inp .rember input {
  outline: 0;
  width: 30px;
  height: 45px;
  border-radius: 4px;
  border: 1px solid #d9d9d9;
  text-indent: 20px;
  font-size: 14px;
  background: #fff !important;
}

.inp .rember p span {
  display: inline-block;
  font-size: 12px;
  width: 100px;
  /*position: absolute;*/
  /*left: 20px;*/
}
#geetest {
  margin-top: 20px;
}
.register_btn {
  width: 100%;
  height: 45px;
  background: #84cc39;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
  letter-spacing: 0.26px;
  margin-top: 30px;
}
.inp .go_login {
  text-align: center;
  font-size: 14px;
  color: #9b9b9b;
  letter-spacing: 0.26px;
  padding-top: 20px;
}
.inp .go_login span {
  color: #84cc39;
  cursor: pointer;
}
#geetest1 {
  margin-top: 15px;
}
</style>
