<script setup>
import { onMounted, onUpdated, ref } from "vue";
import { useRoute, useRouter } from "vue-router";

// Cutom imports
import { updatePlayers } from "@/utils/composabels/playersApi";

// Reactive states
const teamParam = ref(null);
const message = ref(null);
const players = ref([]);
const error = ref(null);
const team = ref("");

// Hooks
const { data: newData, error: updatePlayerError, update } = updatePlayers();
const router = useRouter();
const route = useRoute();

/**
 * Function to handle players update
 */
const handleSubmit = async () => {
  // Validations
  for (let index = 0; index < players.value.length; index++) {
    let player = players.value[index];

    if (!player.username) {
      error.value = `Missing username at row ${index + 1}`;
      break;
    } else if (!player.name) {
      error.value = `Missing name at row ${index + 1}`;
      break;
    } else if (!player.email) {
      error.value = `Missing email at row ${index + 1}`;
      break;
    } else {
      error.value = null;
    }
  }

  if (error.value) {
    return;
  } else {
    error.value = null;
    let payload = [];

    players.value.forEach((player, index) => {
      let p = {
        id: player.id,
        teamName: teamParam.value,
        name: player.name,
        username: player.username,
        email: player.email,
      };
      payload.push(player);
    });

    if (payload.length > 0) {
      let resOk = await update({ players: payload });

      if (resOk) {
        message.value = "Players updated successfully";
      }
    } else {
      error.value = "Something went wrong";
    }
  }

  if (updatePlayerError) {
    error.value = updatePlayerError;
  }
};

/**
 * Get players data whwn component is mounted
 */
onMounted(() => {
  let p = JSON.parse(localStorage.getItem("players"));

  if (!p) {
    router.push("/");
  } else {
    teamParam.value = route.params.team;
    players.value = p[teamParam.value];
  }
});

/**
 * Perform operations when states are updated
 */
onUpdated(() => {
  console.log("team", team.value);
  console.log("players", players.value);
});
</script>

<template>
  <div class="flex flex-col items-center justify-center">
    <h1 class="text-lg font-bold text-gray-700 tracking-wider my-10">
      Update Players
    </h1>

    <div class="bg-white shadow-lg py-7 px-5 rounded-xl w-[80dvw] mb-10">
      <!-- Add team name -->
      <div>
        <input
          :value="teamParam"
          type="text"
          placeholder="Team Name"
          class="w-full border border-gray-400 focus-within:border-gray-600 outline-none px-3 py-2 rounded-lg text-gray-500 pointer-events-none opacity-80"
        />
      </div>

      <!-- Add players -->
      <div class="w-full mt-10 flex flex-col items-center justify-center gap-5">
        <!-- Add new players input fields -->
        <div
          v-for="(player, index) in players"
          :key="index"
          class="w-full flex items-center justify-center gap-4"
        >
          <input
            v-model="player.username"
            type="text"
            placeholder="Username"
            class="w-full border border-gray-400 focus-within:border-gray-600 outline-none px-3 py-2 rounded-lg text-gray-500"
            required
          />
          <input
            v-model="player.name"
            type="text"
            placeholder="Player Name"
            class="w-full border border-gray-400 focus-within:border-gray-600 outline-none px-3 py-2 rounded-lg text-gray-500"
            required
          />
          <input
            v-model="player.email"
            type="email"
            placeholder="Player Email"
            class="w-full border border-gray-400 focus-within:border-gray-600 outline-none px-3 py-2 rounded-lg text-gray-500"
            required
          />
        </div>

        <div v-if="error" class="text-sm text-red-500">{{ error }}</div>
        <div v-if="message" class="text-sm text-green-500">{{ message }}</div>

        <button
          @click="handleSubmit"
          class="flex items-center justify-center self-end mb-5 text-sm gap-2 px-3 py-2 bg-blue-600 rounded-xl hover:bg-blue-700 transition-all duration-300 cursor-pointer text-gray-100"
        >
          Submit
        </button>
      </div>
    </div>
  </div>
</template>
