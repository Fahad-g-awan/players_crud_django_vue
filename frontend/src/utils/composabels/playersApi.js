import { ref } from "vue";

import api from "../api";

export const fetchPlayers = () => {
  const data = ref(null);
  const error = ref(null);

  const load = async () => {
    try {
      const response = await api.get("/players");
      console.log("Fethc players API esponse:", response.data);

      data.value = response.data;
    } catch (err) {
      console.log("Error:", err);

      error.value = err?.response?.data?.error || "Something went wring";
    }
  };

  return { data, error, load };
};

export const addPlayers = () => {
  const data = ref(null);
  const error = ref(null);

  const add = async (payload) => {
    try {
      const response = await api.post("/players", payload);
      console.log("Add players API esponse:", response.data);

      data.value = response.data;
      return true;
    } catch (err) {
      console.log("Error:", err);

      error.value = err?.response?.data?.error || "Something went wring";
    }
  };

  return { data, error, add };
};

export const updatePlayers = () => {
  const data = ref(null);
  const error = ref(null);

  const update = async (payload) => {
    try {
      const response = await api.put("/players", payload);
      console.log("Ipdate players API esponse:", response.data);

      data.value = response.data;
      return true;
    } catch (err) {
      console.log("Error:", err);

      error.value = err?.response?.data?.error || "Something went wring";
    }
  };

  return { data, error, update };
};

export const deletePlayers = () => {
  const data = ref(null);
  const error = ref(null);

  const deletePlayer = async (payload) => {
    try {
      console.log("payload", payload);
      const response = await api.delete("/players", { data: payload });
      console.log("Ipdate players API esponse:", response.data);

      data.value = response.data;
      return true;
    } catch (err) {
      console.log("Error:", err);

      error.value = err?.response?.data?.error || "Something went wring";
    }
  };

  return { data, error, deletePlayer };
};
