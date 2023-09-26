<template>
  <h1 class="mb-12">Vue + Python Websockets</h1>
  <div>
    <input v-model="message" type="text" class="p-3 mr-3 rounded-lg" />
    <button @click="send">Send</button>
  </div>
  <div class="mt-6">
    <div
      v-for="msg in recievedMessages"
      class="p-3 mb-1 bg-gray-100 text-slate-900 rounded-lg"
    >
      {{ msg }}
    </div>
  </div>
</template>
<script setup lang="ts">
import { ref } from "vue";

const websocket = new WebSocket("wss://playground.tanssw.com/wss");

const message = ref("");
const recievedMessages = ref<string[]>([]);
function send() {
  websocket.send(message.value);
  message.value = "";
}

websocket.onmessage = (event) => {
  recievedMessages.value.push(event.data as string);
};
</script>
