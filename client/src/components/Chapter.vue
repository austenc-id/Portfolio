<template>
    <section class="chapter">
        <h1 class="title" v-html="chapter.title"></h1>
        <StoryNav :stories="chapter.stories" />

    </section>
</template>

<script>
import StoryNav from './Chapter/StoryNav'

export default {
    name: 'Chapter',
    components: {
        StoryNav,
    },
    props: {
        chapter: Object,
    },
}

</script>