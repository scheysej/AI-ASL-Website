<template>
  <main class="grid grid-cols-4 gap-5">
    <section class="col-span-3">
      <div class="h-30 flex items-center">
        <h1 class="font-semibold text-2xl mb-0 text-gray-600">
          American Sign Language (ASL) Prediction
        </h1>
      </div>
      <video
        id="video"
        autoplay
        playsinline
        class="w-full h-[calc(100vh-140px)] bg-gray-100 rounded-lg"
      ></video>
    </section>
    <section class="rounded-lg flex flex-col">
      <!-- <p class="h-25">Modes</p> -->
      <div class="h-30 flex items-center w-full">
        <div
          class="shadow-sm w-full overflow-auto justify-around rounded-full flex items-center h-20 gap-4"
        >
          <div class="flex items-center gap-4">
            <span
              class="w-22 flex flex-col items-center h-13 justify-between cursor-pointer"
              @click="selection = 'Alphabet'"
            >
              <img
                src="@/assets/alphabet-level.png"
                alt="Alphabet level"
                class="w-8 rounded-full transition-all duration-250 border p-1 border-white"
                :class="{ selected: selection === 'Alphabet' }"
              />
              <p class="text-[12px] font-medium text-gray-600 text-center">Alphabet level</p>
            </span>
            <span
              class="w-22 flex flex-col items-center h-13 justify-between cursor-pointer"
              @click="selection = 'Word'"
            >
              <img
                src="@/assets/word-level.png"
                alt="Word level"
                class="w-8 rounded-full transition-all duration-250 border p-1 border-white"
                :class="{ selected: selection === 'Word' }"
              />
              <p class="text-[12px] font-medium text-gray-600 text-center">Word level</p>
            </span>
            <span
              class="w-22 flex flex-col items-center h-13 justify-between cursor-pointer"
              @click="selection = 'Lip'"
            >
              <img
                src="@/assets/lip-reading.png"
                alt="Lip reading"
                class="w-8 rounded-full transition-all duration-250 border p-1 border-white"
                :class="{ selected: selection === 'Lip' }"
              />
              <p class="text-[12px] font-medium text-gray-600 text-center">Lip reading</p>
            </span>
            <span
              class="w-22 flex flex-col items-center h-13 justify-between cursor-pointer"
              @click="selection = 'Emotion'"
            >
              <img
                src="@/assets/emotion-reading.png"
                alt="Emotion detection"
                class="w-8 rounded-full transition-all duration-250 border p-1 border-white"
                :class="{ selected: selection === 'Emotion' }"
              />
              <p class="text-[12px] font-medium text-gray-600 text-center">Emotion</p>
            </span>
          </div>
        </div>
      </div>
      <article class="h-83 w-full rounded-lg py-5 flex items-center flex-col justify-between">
        <div class="flex justify-between w-full">
          <p class="font-medium">Prediction:</p>
          <p class="font-medium">Confidence: 10%</p>
        </div>
        <p class="text-9xl my-0">{{ prediction }}</p>
        <progress class="w-[90%] rounded-full" value="10" max="100"></progress>
      </article>
      <section class="mt-10">
        <p class="font-medium">Other possible predictions:</p>
        <div class="mt-4 flex gap-4 flex-wrap">
          <div class="max-w-36 bg-white px-3 rounded-md py-3">
            <p class="font-medium">S</p>
            <progress class="w-full rounded-full mt-4" value="5" max="100"></progress>
          </div>
          <div class="max-w-36 bg-white px-3 rounded-md py-3">
            <p class="font-medium">T</p>
            <progress class="w-full rounded-full mt-4" value="50" max="100"></progress>
          </div>
        </div>
      </section>
    </section>
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

type Modes = 'Alphabet' | 'Word' | 'Lip' | 'Emotion'
const prediction = ref<string>('A')
const selection = ref<Modes>('')

onMounted(() => {
  const video = document.getElementById('video') as HTMLVideoElement

  if (video) {
    navigator.mediaDevices
      .getUserMedia({ video: true, audio: false })
      .then((stream) => {
        video.srcObject = stream
      })
      .catch((err) => {
        console.error('Error accessing webcam:', err)
      })
  } else {
    console.error('Video element not found.')
  }
})
</script>

<style>
.selected {
  padding: 4px;
  border: solid 1px rgb(203, 203, 203);
  border-radius: 100px;
}
</style>
