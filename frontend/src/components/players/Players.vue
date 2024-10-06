<script setup>
import { useRoute, useRouter } from "vue-router";
import { onMounted, ref } from "vue";

// Icons
import { PenLine, Trash2 } from "lucide-vue-next";

// Custom imports
import {
  deletePlayers,
  fetchPlayers,
} from "../../utils/composabels/playersApi.js";

// Reactive states
const errorMessage = ref(null);
const message = ref(null);

// Hooks
const { deletePlayer, error: deleteError } = deletePlayers();
const { data, error: fetchError, load } = fetchPlayers();
const router = useRouter();
const route = useRoute();

/**
 * Function to redirect user to update page for the specific selected team
 *
 * @param {string} team - Player team name
 */
const handleUpdate = (team) => {
  router.push("/update-players/" + team);
};

/**
 * Functio to handle player delete operations
 *
 * @param {String} playerId - Id of the player which will be deleted
 */
const handleDeletePlayer = async (playerId) => {
  if (playerId) {
    let resOk = await deletePlayer({ id: playerId });

    if (resOk) {
      message.value = "Players updated successfully";
      await load();
    }
  }

  if (deleteError) {
    errorMessage.value = deleteError;
  }
};

/**
 * Get players data whwn component is mounted
 */
onMounted(async () => {
  await load();

  if (data.value) {
    localStorage.setItem("players", JSON.stringify(data.value));
  }

  if (fetchError) {
    errorMessage.value = fetchError;
  }
});
</script>

<template>
  <div class="flex flex-col items-center justify-center">
    <h1 class="text-lg font-bold text-gray-700 tracking-wider my-10">
      All Players
    </h1>

    <div
      v-if="data"
      class="w-[80dvw] flex flex-col items-center justify-center gap-5 bg-blue-300 p-4 rounded-2xl mb-10"
    >
      <div
        :class="{
          'w-full flex items-center justify-center gap-5 pb-2': true,
          'border-b border-gray-400': true,
        }"
      >
        <div class="w-full flex items-center justify-center">TEAM</div>
        <div class="w-full flex items-center justify-center">ID</div>
        <div class="w-full flex items-center justify-start">USERNAME</div>
        <div class="w-full flex items-center justify-start capitalize">
          FULL NAME
        </div>
        <div class="w-full flex items-center justify-start">EMAIL</div>
        <div class="w-full flex items-center justify-start">DELETE PLAYER</div>
        <div class="w-full flex items-center justify-start">UPDATE PLAYERS</div>
      </div>

      <div v-for="(players, team, index) in data" :key="index" class="w-full">
        <div
          :class="{
            'w-full text-gray-600 flex items-center justify-start gap-5': true,
            'bg-blue-200 py-3 px-4 rounded-xl cursor-pointer': true,
          }"
        >
          <!-- Team name -->
          <div class="w-52 flex items-center justify-center capitalize">
            {{ team }}
          </div>

          <!-- Team's players details -->
          <div class="w-full flex flex-col items-center justify-center gap-5">
            <div
              v-for="(player, pIndex) in players"
              :key="pIndex"
              :class="{
                'w-full flex items-center justify-center gap-5 pb-2': true,
                'border-b border-gray-400': pIndex != players.length,
              }"
            >
              <div class="w-24 flex items-center justify-center">
                {{ player.id }}
              </div>
              <div class="w-full flex items-center justify-start">
                {{ player.username }}
              </div>
              <div class="w-full flex items-center justify-start capitalize">
                {{ player.name }}
              </div>
              <div class="w-full flex items-center justify-start">
                {{ player.email }}
              </div>
              <div class="w-full flex items-center justify-start">
                <Trash2
                  @click="handleDeletePlayer(player.id)"
                  class="size-4 text-red-600 cursor-pointer hover:text-red-700"
                />
              </div>
            </div>
          </div>

          <div class="w-24 flex items-center justify-center">
            <PenLine
              @click="handleUpdate(team)"
              class="size-4 text-green-600 cursor-pointer hover:text-green-700"
            />
          </div>
        </div>
      </div>

      <div v-if="message" class="text-sm text-green-500 my-5">
        {{ message }}
      </div>
      <div v-if="errorMessage" class="text-sm text-red-500 my-5">
        {{ errorMessage }}
      </div>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>
