/* eslint-disable */

import service from "../utils/requests.js";

// http://axios-js.com/zh-cn/docs/#%E8%AF%B7%E6%B1%82%E9%85%8D%E7%BD%AE
export function GetCates () {
  return service.request({
    url: '/books_cates',
    method: 'get'
  })
}

export function registerFrom (data) {
  return service.request({
    url: "/register/",
    method: 'post',
    withCredentials: true,
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      // "X-CSRFToken": this.submitToken,
      // "X-CSRFToken": document.cookie,
    },
    data: JSON.stringify(data)
  })
}

export function formToken () {
  return service.request({
    url: '/token/',
    method: 'get',
  })
}

// 注销用户
export function logOut (data) {
  return service.request({
    url: '/logout/',
    method: 'get',
  })
}

