<template>
    <nav class="chapters">
        <h3 v-for="chapter in chapters" :id="'chapter-' + chapter.id" class="link" @click="renderChapter(chapter)" v-html="chapter.title">
        </h3>
    </nav>
    <Chapter :key="key" v-if="active.chapter" :chapter="active.chapter" />

</template>

<script>
import Chapter from './Chapter'

export default {
    name: 'Navbar',
    components: {
        Chapter,
    },
    created() {
        this.renderChapter(this.chapters[0])
    },
    data() {
        return this.$store.state
    },
    methods: {
        keyChange() {
            this.key++
        },
        async renderChapter(chapter) {
            this.keyChange()
            // chapter.stories.sort(utils.compareIDs)
            this.active.chapter = chapter
            // utils.resetActiveElements()
            // await utils.sleep(.01)
            //     .then(timer => {
            //         document.getElementById(`chapter-${chapter.id}`).classList.add('active')
            //     })
        },
    }
}

</script>