<template>
    <nav class="stories">
        <h4 v-for="story in active.chapter.stories" :id="'story-' + story.id" @click="renderStory(story)" class="link story">
            {{ story.title }}
        </h4>
    </nav>
    <Story v-if="active.story" :story="active.story" />
</template>

<script>
import Story from './Story'


export default {
    name: 'StoryNav',
    components: {
        Story,
    },
    mounted() {
        this.renderStory(this.active.chapter.stories[0])
    },
    updated() {
    },
    data() {
        return this.$store.state
    },
    methods: {
        async renderStory(story) {
            // story.paragraphs.sort(utils.compareIDs)
            this.active.story = story
            // await utils.sleep(.01)
            //     .then(timer => {
            //         document.getElementById(`story-${story.id}`).classList.add('active')
            //     })
        },
    }
}

</script>