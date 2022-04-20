<template>

    <header>
        <div class="titles">
            <h1 class="title">{{ titles.title }}</h1>
            <h2 class="title">{{ titles.subTitle }}</h2>
        </div>
        <div class="links">
            <a v-for="link in links" :href="link.url" v-html="link.icon" target="_blank" class="link">
            </a>
        </div>
    </header>

</template>

<script>
export default {
    name: 'Header',
    props: {
        titles: Object,
        links: Object,
    }
}
</script>