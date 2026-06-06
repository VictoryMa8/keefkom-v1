<script setup lang="ts">
import { onMounted } from 'vue'
import TestButton from './TestButton.vue'
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

onMounted(() => {
  const map = new maplibregl.Map({
    container: 'map', // container id
    style: 'https://demotiles.maplibre.org/style.json', // style URL
    center: [0, 0], // starting position [lng, lat]
    zoom: 1, // starting zoom
    maplibreLogo: true
  });
})

</script>

<template>
  <h1 class="text-center mt-4 text-2xl font-[Alegraya]">Keefkom كيفكم v1</h1>
  <div class="flex flex-col items-center">
    <div id="map" class="my-4 w-8/10 h-[500px] border-4 border-primary"></div>
  </div>
  <TestButton />
</template>

<style scoped></style>
