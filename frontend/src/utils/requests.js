/* eslint-disable */

import axios from "axios";
import store from "@/store/index"; 

// console.log("in request.js", process.env.NODE_ENV);

// console.log("in request.js", process.env.VUE_APP_URL);

// axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? '' : '/api';  //关键代码
const BASEURL = process.env.NODE_ENV === 'production' ? '/api' : '/api'
// console.log("in request.js: BASEURL = ", BASEURL);

/* 
自定义写法：const xxx = axios.create({}) 一个项目中可能有不同的服务器基础地址 就要用自定义写法设置不同的服务器基础地址 
*/ 

// 创建axios  axios.create(config) 对axios请求进行二次封装
const service = axios.create({
  baseURL: BASEURL,
  timeout: 1800000
})

const instance = axios.create({
  baseURL: BASEURL,
  timeout: 1800000
})


// 请求拦截器： 在浏览器发送请求之前的处理; 用处：对真的发送请求之前可以判断，比如是否合法，是否符合请求参数的要求
service.interceptors.request.use(
  function (config) {
    console.log('request.js: request:  config===== ', config)
    return config
  },
  function (error) {
    return Promise.reject(error)
  }
)

// 响应拦截器： 服务器返回数据后处理
service.interceptors.response.use(
  function (response) {
    console.log('request.js: response = ', response)
    const data = response.data
    if (data.resCode !== 0) {
      // 服务器有响应，但是并不是想要的数据
      // Message.error(data.message);
      console.log('request.js: 服务器有响应，但是并不是想要的数据')
      return Promise.reject(data.resCode)
      // return response
    } else {
      // 服务器有响应，并且数据正确
      console.log('request.js: 服务器有响应，并且数据正确')
      console.log('request.js: data.data = ', data.data)
      return response
    }

    // return response;
  },
  function (error) {
    // 服务器没有响应 404,405
    return Promise.reject(error)
  }
)

// 在instance(这是上面定义的自定义axios请求名称)上添加请求拦截器 补充请求头token信息 
instance.interceptors.request.use(
  function(config) {
    // 从vuex中取出token,这里先这样写，下面会说这里是怎么回事 
    const token = store.state.token; 
    // 如果有token则添加到headers中 
    if (token) {  //这里的JWT是后端默认的token需要携带的字段，可在后端自定义，中间空格不能删除 }
      config.headers.Authorization = `JWT ${token}`;
      return config; 
    }
  },
  function(error) {
     return Promise.reject(error); 
    }
)


// 对外暴露接口
export default service;
