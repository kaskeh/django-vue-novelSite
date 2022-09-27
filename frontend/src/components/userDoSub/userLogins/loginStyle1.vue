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
            :class="login_type == 0 ? 'current' : ''"
            @click="login_type = 0"
          >
            密码登录
          </span>
          <span
            :class="login_type == 1 ? 'current' : ''"
            @click="login_type = 1"
          >
            短信登录
          </span>
        </div>
        <div class="inp" v-if="login_type == 0">
          <input
            v-model="username"
            type="text"
            placeholder="用户名 / 手机号码"
            class="user"
          />
          <input
            v-model="password"
            type="password"
            name=""
            class="pwd"
            placeholder="密码"
          />
          <div id="geetest1"></div>
          <div class="rember">
            <p>
              <input type="checkbox" class="no" v-model="remember" />
              <span>记住密码</span>
            </p>
            <p>忘记密码</p>
          </div>
          <button class="login_btn" @click="loginHandle">登录</button>
          <p class="go_login">
            没有账号
            <span>
              <router-link to="/register">立即注册</router-link>
            </span>
          </p>
        </div>
        <div class="inp" v-show="login_type == 1">
          <input
            v-model="username"
            type="text"
            placeholder="手机号码"
            class="user"
          />
          <input
            v-model="password"
            type="text"
            class="pwd"
            placeholder="短信验证码"
          />
          <button id="get_code">获取验证码</button>
          <button class="login_btn">登录</button>
          <p class="go_login">
            没有账号
            <span>
              <router-link to="/register">立即注册</router-link>
            </span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import instance from "@/utils/login_request";
export default {
  name: "loginComp",
  data() {
    return {
      login_type: 0,
      username: "",
      password: "",
      remember: false, // 是否记住密码
    };
  },

  methods: {
    loginHandle() {
      // console.log("点击了登录");
      // 登陆处理
      instance
        .post("/login/", {
          username: this.username,
          password: this.password,
        })
        // this.$axios
        //   .post(`${this.$settings.Host}/users/login/`, {
        //     username: this.username,
        //     password: this.password,
        //   })
        .then((res) => {
          console.log(res.data);
          // 登陆成功
          if (this.remember) {
            // console.log("记住密码了");
            // 记住密码
            localStorage.user_token = res.data.token;
            localStorage.user_id = res.data.userid;
            localStorage.user_name = res.data.username;
            sessionStorage.removeItem("user_token");
            sessionStorage.removeItem("user_id");
            sessionStorage.removeItem("user_name");
          } else {
            // console.log("不记住密码了");
            // 不记住密码
            sessionStorage.user_token = res.data.token;
            sessionStorage.user_id = res.data.userid;
            sessionStorage.user_name = res.data.username;
            localStorage.removeItem("user_token");
            localStorage.removeItem("user_id");
            localStorage.removeItem("user_name");
          }

          // sessionStorage.user_credit = res.data.user_credit;
          // sessionStorage.credit_rmb = res.data.credit_rmb;

          let self = this;
          self.$alert(`欢迎回来！`, `可容书阁`, {
            callback() {
              // 返回本页
              self.$router.go(0);
            },
          });
        })
        .catch((error) => {
          // 登陆失败
          document.getElementById("geetest1").innerHTML = "";
          this.$message.error("对不起，账号或密码错误！");
          // console.log("登录失败");
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
.login_btn {
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
