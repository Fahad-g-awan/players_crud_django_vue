import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AddPlayersView from "@/views/AddPlayersView.vue";
import UpdatePlayersView from "@/views/UpdatePlayersView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/add-players",
      name: "Add Players",
      component: AddPlayersView,
    },
    {
      path: "/update-players/:team",
      name: "Update Players",
      component: UpdatePlayersView,
    },
  ],
});

export default router;
