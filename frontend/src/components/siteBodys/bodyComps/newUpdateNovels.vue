<template>
  <div id="lastUpdate">
    <b-container class="mt-4 mb-2">
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
                    <div>小说分类</div>
                  </th>
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="2"
                    class=""
                  >
                    <div>小说</div>
                  </th>
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="3"
                    class=""
                  >
                    <div>小说作者</div>
                  </th>
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="4"
                    class=""
                  >
                    <div>最新章节</div>
                  </th>
                  <th
                    role="columnheader"
                    scope="col"
                    aria-colindex="5"
                    class=""
                  >
                    <div>更新时间</div>
                  </th>
                </tr>
              </thead>
              <tbody role="rowgroup">
                <tr role="row" v-for="item in items.newestItems" :key="item.id">
                  <td aria-colindex="1" role="cell" class="">
                    <!-- <a :href="'/book/' + item.book_id">
                      {{ item.book_name }}
                    </a> -->
                    <p>{{ item.book_cate }}</p>
                  </td>
                  <td aria-colindex="2" role="cell" class="">
                    <a
                      :href="
                        '/book/' + item.book_id + '/' + item.book_newest_url
                      "
                    >
                      {{ item.book_name }}
                    </a>
                  </td>
                  <td aria-colindex="3" role="cell" class="">
                    <!-- {{ dateFormat(item.book_last_update_time) }} -->
                    {{ item.book_author }}
                  </td>
                  <td aria-colindex="4" role="cell" class="">
                    <a
                      :href="
                        '/book/' + item.book_id + '/' + item.book_newest_url
                      "
                    >
                      {{ item.book_newest_name }}
                    </a>
                  </td>
                  <td aria-colindex="5" role="cell" class="">
                    <!-- {{ dateFormat(item.book_last_update_time) }} -->
                    {{ item.book_last_update_time }}
                  </td>
                </tr>
              </tbody>
            </table>
          </b-col>
          <b-col cols="12" md="1"></b-col>
          <b-col cols="12" md="4">
            <h4>最多阅读的小说</h4>
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
                    <div>作者</div>
                  </th>
                </tr>
              </thead>
              <tbody role="rowgroup">
                <tr role="row" v-for="item in items.mostItems" :key="item.id">
                  <td aria-colindex="1" role="cell" class="">
                    <a :href="'/book/' + item.book_id">
                      {{ item.book_name }}
                    </a>
                  </td>
                  <td aria-colindex="2" role="cell" class="">
                    <a
                      :href="
                        '/book/' + item.book_id + '/' + item.book_newest_url
                      "
                    >
                      {{ item.book_author }}
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>
          </b-col>
        </b-row>
      </div>
    </b-container>
  </div>
</template>
<script>
import { ref, reactive, onMounted } from "vue";
import { useRouter } from "vue-router";
// import { ref, reactive, onMounted } from "@vue/composition-api";
export default {
  name: "lastUpdate",
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

  setup(props, context) {
    // const now_url = ref(this.$router.path); vue2获取当前路径的写法
    const now_url = useRouter().currentRoute.value.fullPath;
    console.log("当前url", now_url);

    // const newstParams = reactive({
    //   url: now_url.value,
    //   key: "newest",
    // });

    // const mostParams = reactive({
    //   url: now_url.value,
    //   key: "most",
    // });

    // const items = reactive({
    //   newestItems: [],
    //   mostItems: [],
    // });
  },
};
</script>
