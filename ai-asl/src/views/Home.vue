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
    <section class="rounded-lg flex">
      <div class="h-30 flex items-center w-full">
        <div class="shadow-sm w-full justify-around rounded-full flex items-center h-20 gap-4">
          <p class="font-semibold text-gray-600">Modes</p>
          <div class="flex items-center gap-4">
            <span class="w-22 flex flex-col items-center h-13 justify-between">
              <img src="@/assets/alphabet-level.png" alt="Alphabet level" class="w-7" />
              <p class="text-[12px] font-medium text-gray-600 text-center">Alphabet level</p>
            </span>
            <span class="w-22 flex flex-col items-center h-13 justify-between">
              <img src="@/assets/word-level.png" alt="Word level" class="w-8.5" />
              <p class="text-[12px] font-medium text-gray-600 text-center">Word level</p>
            </span>
            <span class="w-22 flex flex-col items-center h-13 gap-3">
              <img src="@/assets/lip-reading.png" alt="Lip reading" class="w-4" />
              <p class="text-[12px] font-medium text-gray-600 text-center">Lip reading</p>
            </span>
            <span class="w-22 flex flex-col items-center h-13 gap-3">
              <img src="@/assets/emotion-reading.png" alt="Emotion detection" class="w-8" />
              <p class="text-sm font-medium text-gray-600 text-center">Emotion detection</p>
            </span>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'

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
