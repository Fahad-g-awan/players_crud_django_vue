<script setup>
import { onUpdated, ref } from "vue";
import { X, Plus } from "lucide-vue-next";
import { addPlayers } from "@/utils/composabels/playersApi";

const defaultPlayer = {
  team_name: "",
  username: "",
  name: "",
  email: "",
};

const players = ref([{ ...defaultPlayer }]);
const message = ref(null);
const error = ref(null);
const team = ref("");

const { data: newData, error: addPlayerError, add } = addPlayers();

const handleAddPlayer = () => {
  players.value.push({ ...defaultPlayer });
};

const handleRemovePlayer = (index) => {
  console.log("remove index", index);

  players.value = players.value.filter((player, i) => i != index);
};

const handleSubmit = async () => {
  // Validations
  if (!team.value.trim()) {
    error.value = `Please add team name`;
    return;
  } else {
    error.value = null;
  }

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
    let payload = [];

    players.value.forEach((player, index) => {
      player.team_name = team;
      payload.push(player);
    });

    if (payload.length > 0) {
      let resOk = await add({ players: payload });

      if (resOk) {
        message.value = "Players added successfully";
        players.value = [{ ...defaultPlayer }];
      }
    } else {
      error.value = "Something went wrong";
    }
  }

  if (addPlayerError) {
    error.value = addPlayerError;
  }
};

// onUpdated(() => {
//   console.log("team", team.value);
//   console.log("players", players.value);
// });
</script>

<template>
  <div class="flex flex-col items-center justify-center">
    <h1 class="text-lg font-bold text-gray-700 tracking-wider my-10">
      Add Players
    </h1>

    <div class="bg-white shadow-lg py-7 px-5 rounded-xl w-[80dvw] mb-10">
      <!-- Add team name -->
      <div>
        <input
          v-model="team"
          type="text"
          placeholder="Team Name"
          class="w-full border border-gray-400 focus-within:border-gray-600 outline-none px-3 py-2 rounded-lg text-gray-500"
        />
      </div>

      <!-- Add players -->
      <div class="w-full mt-10 flex flex-col items-center justify-center gap-5">
        <!-- Add new row for player button -->
        <div
          @click="handleAddPlayer"
          class="flex items-center justify-center self-end mb-5 text-sm gap-2 px-3 py-2 bg-gray-300 rounded-xl hover:bg-gray-400 transition-all duration-300 cursor-pointer text-gray-800 hover:text-gray-700"
        >
          <Plus class="size-5" />
          <span>Add Row</span>
        </div>

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
          <div>
            <X
              @click="handleRemovePlayer(index)"
              class="text-red-500 hover:text-red-700 transition-all duration-300 cursor-pointer"
            />
          </div>
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
