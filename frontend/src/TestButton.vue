<script setup lang="ts">
// script w/ setup: Vue3's composition API, runs once when the component is created
// Everything declared in this is automatically available in the <template>
import { ref } from 'vue'
import { fetchNews, type Article } from './api'

// GNews only supports these countries
const COUNTRIES = [
    { code: 'au', name: 'Australia' },
    { code: 'br', name: 'Brazil' },
    { code: 'ca', name: 'Canada' },
    { code: 'cn', name: 'China' },
    { code: 'eg', name: 'Egypt' },
    { code: 'fr', name: 'France' },
    { code: 'de', name: 'Germany' },
    { code: 'gr', name: 'Greece' },
    { code: 'hk', name: 'Hong Kong' },
    { code: 'in', name: 'India' },
    { code: 'ie', name: 'Ireland' },
    { code: 'it', name: 'Italy' },
    { code: 'jp', name: 'Japan' },
    { code: 'nl', name: 'Netherlands' },
    { code: 'no', name: 'Norway' },
    { code: 'pk', name: 'Pakistan' },
    { code: 'pe', name: 'Peru' },
    { code: 'ph', name: 'Philippines' },
    { code: 'pt', name: 'Portugal' },
    { code: 'ro', name: 'Romania' },
    { code: 'ru', name: 'Russia' },
    { code: 'sg', name: 'Singapore' },
    { code: 'es', name: 'Spain' },
    { code: 'se', name: 'Sweden' },
    { code: 'ch', name: 'Switzerland' },
    { code: 'tw', name: 'Taiwan' },
    { code: 'ua', name: 'Ukraine' },
    { code: 'gb', name: 'United Kingdom' },
    { code: 'us', name: 'United States' },
]

// ref() wraps a value so Vue can track changes to it
const articles = ref<Article[]>([])
const isLoading = ref(false)
const selected = ref('au')

async function loadArticles() {
    isLoading.value = true
    articles.value = await fetchNews(selected.value)
    isLoading.value = false
}
</script>

<template>
    <div class="flex flex-col items-center justify-center mt-4">
        <!-- 
         v-model is Vue's way of a two-way binding
         Sets the select element's value to selected.value and
         updates selected.value to whatever the user picks 
        -->
        <select v-model="selected" class="select select-primary">
            <option v-for="c in COUNTRIES" :value="c.code" :key="c.code">{{ c.name }}</option>
        </select>
        <button v-if="!isLoading" class="btn btn-primary mt-4" @click="loadArticles()">Trending News From {{ COUNTRIES.find(c => c.code === selected)?.name }}</button>
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