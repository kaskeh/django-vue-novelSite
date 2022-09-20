<template>
  <div id="HomeCate">
    <Header />

    <b-container class="mt-4 mb-2">
      <!-- 添加一个面包屑导航栏 -->
      <el-breadcrumb :separator-icon="ArrowRight">
        <el-breadcrumb-item :to="{ path: '/' }">可容书阁</el-breadcrumb-item>
        <el-breadcrumb-item>玄幻</el-breadcrumb-item>
      </el-breadcrumb>

      <br />

      <div v-if="items.newestItems.length == 0">您要查询的分类页面不存在哦</div>
      <div v-else>
        <b-row>
          <b-col cols="12" md="7">
            <h4>最新更新的小说</h4>
            <table
              role="table"
              aria-busy="false"
              aria-colcount="3"
              class="table b-table table-striped table-hover"
            >
              <thead role="rowgroup" class="">
                <tr role="row" class="">
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="1"
                    class=""
                  >
                    <div>小说</div>
                  </th>
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="2"
                    class=""
                  >
                    <div>最新章节</div>
                  </th>
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="3"
                    class=""
                  >
                    <div>更新时间</div>
                  </th>
                </tr>
              </thead>
              <tbody role="rowgroup">
                <tr role="row" v-for="item in items.newestItems" :key="item.id">
                  <td aria-colindex="1" role="cell" class="">
                    <a :href="'/book/' + item.book_id">{{ item.book_name }}</a>
                  </td>
                  <td aria-colindex="2" role="cell" class="">
                    <a
                      :href="
                        '/book/' + item.book_id + '/' + item.book_newest_url
                      "
                    >
                      {{ item.book_newest_name }}
                    </a>
                  </td>
                  <td aria-colindex="3" role="cell" class="">
                    {{ item.book_last_update_time }}
                  </td>
                </tr>
              </tbody>
            </table>
          </b-col>
          <b-col cols="12" md="1"></b-col>
        </b-row>
      </div>

      <!-- 添加个分页功能 -->
      <br />
      <el-pagination background layout="prev, pager, next" :total="1000" />
    </b-container>
    <Footer />
  </div>
</template>

<script>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";

import { ArrowRight } from "@element-plus/icons-vue";

import Header from "../components/siteHeaders/headerStyle0.vue";
import Footer from "../components/siteFooters/footerStyle0.vue";
export default {
  name: "HomeCate",
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      items: {
        newestItems: [
          {
            book_cate: "玄幻",
            book_id: "999",
            book_name: "之上学",
            book_author: "许嵩",
            book_newest_name: "第一千章",
            book_last_update_time: "2020-08-01",
          },
          {
            book_cate: "玄幻",
            book_id: "999",
            book_name: "之上学",
            book_author: "许嵩",
            book_newest_name: "第一千章",
            book_last_update_time: "2020-08-01",
          },
          {
            book_cate: "玄幻",
            book_id: "999",
            book_name: "之上学",
            book_author: "许嵩",
            book_newest_name: "第一千章",
            book_last_update_time: "2020-08-01",
          },
          {
            book_cate: "玄幻",
            book_id: "999",
            book_name: "之上学",
            book_author: "许嵩",
            book_newest_name: "第一千章",
            book_last_update_time: "2020-08-01",
          },
          {
            book_cate: "玄幻",
            book_id: "999",
            book_name: "之上学",
            book_author: "许嵩",
            book_newest_name: "第一千章",
            book_last_update_time: "2020-08-01",
          },
          {
            book_cate: "玄幻",
            book_id: "999",
            book_name: "之上学",
            book_author: "许嵩",
            book_newest_name: "第一千章",
            book_last_update_time: "2020-08-01",
          },
        ],
        mostItems: [
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
          {
            book_name: "诗画中国",
            book_author: "黄山一",
          },
        ],
      },
    };
  },
  // setup(props, context) {
  //   const router = useRoute();
  //   console.log("router111", router.path);
  //   // onMounted(() => {
  //   //   console.log("In homeCate context:", context);
  //   // });
  // },
};
</script>

<style></style>
