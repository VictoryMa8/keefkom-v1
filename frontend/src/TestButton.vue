<script setup lang="ts">
import { ref } from 'vue'

const articles = ref<any[]>([])
const showBtn = ref(true)

async function fetchArticles() {
    const response = await fetch('/news')
    const json = await response.json()
    articles.value = json.articles
    showBtn.value = false
}

</script>

<template>
    <div class="flex flex-col items-center justify-center mt-4">
        <button v-if="showBtn" class="btn btn-primary" @click="fetchArticles">Get News</button>
        <ul class="list bg-base-100 rounded-box shadow-md  md:w-3/4"> 
            <li v-for="a in articles" :key="a.id" class="list-row">
                <div><img class="w-40 rounded-box" :src="a.image"/></div>
                <div>
                    <p class="text-xl font-[Alegraya] text-primary">{{ a.title }}</p>
                    <p class="text-xl">{{ a.source.name }}</p>
                    <a :href="a.url" class="text-primary hover:cursor-pointer hover:underline text-lg" target="_blank">{{ a.url }}</a>
                </div>
                <p class="list-col-wrap text-lg">{{ a.description }}</p>
            </li>
        </ul>
    </div>
</template>
  
<style scoped></style>