<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  <header>
    <div className="shadow-lg px-10 py-3 w-full">
      <nav class="flex gap-5">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/add-players">Add Players</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
