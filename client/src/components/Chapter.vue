<template>
    <section class="chapter">
        <h1 class="title" v-html="active.chapter.title"></h1>
        <StoryNav :stories="active.chapter.stories" />

    </section>
</template>

<script>
import StoryNav from './Chapter/StoryNav'

export default {
    name: 'Chapter',
    components: {
        StoryNav,
    },
    data(){
        return this.$store.state
    }
}

</script>