import { createRouter, createWebHashHistory } from "vue-router";
export default createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: "/:pathMatch(.*)*",
      component: () => import("../src/components/MainComponents/ErrorFour.vue"),
    },

    {
      path: "/Quetion",
      component: () =>
        import("../src/components/MainComponents/QuetionComp.vue"),
    },
    {
      path: "/main",
      component: () => import("./components/MainComponents/MainComp.vue"),
    },
    {
      path: "/UserInfo",
      component: () => import("./components/СomponetsForPages/UserInfo.vue"),
    },
    {
      path: "/Search",
      component: () => import("./components/СomponetsForPages/SearchComp.vue"),
    },
    {
      path: "/States",
      component: () => import("./States.vue"),
    },
    {
      path: "/Registration",
      component: () =>
        import("./components/СomponetsForPages/RegisterPage.vue"),
    },
    {
      path: "/NewState",
      component: () => import("./NewState.vue"),
    },
    {
      path: "/Quetions",
      component: () => import("./Quetions.vue"),
    },
    {
      path: "/Login",
      component: () => import("./components/СomponetsForPages/EnterPage.vue"),
    },
    {
      path: "/Chat",
      component: () => import("./components/MainComponents/SideChatMenu.vue"),
    },
    {
      path: "/Profile",
      component: () => import("./components/MainComponents/ProfileComp.vue"),
    },
    {
      path: "/ProfileSettings",
      component: () => import("./components/СomponetsForPages/SettingsProfileComp.vue"),
    },
    {
      path: "/Leaders",
      component: () => import("./components/СomponetsForPages/ForumLeader.vue"),
    },
    {
      path: "/Forum",
      component: () => import("./components/СomponetsForPages/Forum.vue"),
    },
    {
      path: "/FAQ",
      component: () => import("./components/СomponetsForPages/FAQ.vue"),
    },
    {
      path: "/CommentsPost",
      component: () => import("./components/CommentsForPost/CommentsPost.vue"),
    },
    {
      path: "/QuestionItem",
      component: () => import("./components/MainComponents/QuestionItem.vue"),
    },
  ],
});
