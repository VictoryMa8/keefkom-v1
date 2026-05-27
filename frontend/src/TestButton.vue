<script setup lang="ts">
// script w/ setup: Vue3's composition API, runs once when the component is created
// Everything declared in this is automatically available in the <template>
import { ref } from 'vue'
import { fetchNews, type Article } from './api'

// ref() wraps a value so Vue can track changes to it
const articles = ref<Article[]>([])
const isLoading = ref(false)

async function loadArticles() {
    isLoading.value = true
    articles.value = await fetchNews('us')
    isLoading.value = false
}
</script>

<template>
    <div class="flex flex-col items-center justify-center mt-4">
        <button v-if="!isLoading" class="btn btn-primary" @click="loadArticles">Get News</button>
        <ul class="list bg-base-100 rounded-box shadow-md  md:w-3/4"> 
            <li v-for="a in articles" :key="a.title" class="list-row">
                <div><img class="w-40 rounded-box" :src="a.image"/></div>
                <div>
                    <p class="text-xl font-[Alegraya] text-primary">{{ a.title }}</p>
                    <a :href="a.url" class="text-primary hover:cursor-pointer hover:underline text-lg" target="_blank">{{ a.url }}</a>
                </div>
                <p class="list-col-wrap text-lg">{{ a.description }}</p>
            </li>
        </ul>
    </div>
</template>
  
<style scoped></style>