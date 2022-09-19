import axios from "axios";
import store from "@/store/index";

const BASEURL = process.env.NODE_ENV === "production" ? "/api" : "/api";

const instance = axios.create({
  baseURL: BASEURL,
  timeout: 1800000,
});

// 在instance(这是上面定义的自定义axios请求名称)上添加请求拦截器 补充请求头token信息
instance.interceptors.request.use(
  function (config) {
    // 从vuex中取出token,这里先这样写，下面会说这里是怎么回事
    const token = store.state.token;
    // 如果有token则添加到headers中
    if (token) {
      //这里的JWT是后端默认的token需要携带的字段，可在后端自定义，中间空格不能删除 }
      // 前端在每次请求时将JWT放入HTTP Header中的Authorization位。(解决XSS和XSRF问题)
      config.headers.Authorization = `JWT ${token}`;
      // console.log("本地有token", token);
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

// 对外暴露接口
export default instance;
