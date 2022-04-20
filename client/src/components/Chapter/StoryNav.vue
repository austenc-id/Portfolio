<template>
    <nav class="stories">
        <h4 v-for="story in stories" :id="'story-' + story.id" @click="renderStory(story)" class="link story">
            {{ story.title }}
        </h4>
    </nav>
    <Story v-if="active.story" :story="active.story" />
</template>

<script>
import { utils } from '../../scripts/utils'
import Story from './Story'


export default {
    name: 'StoryNav',
    props: {
        stories: Array,
        key: Number
    },
    components: {
        Story,
    },
    mounted() {
        this.renderStory(this.stories[0])
    },
    updated() {
    },
    data() {
        return {
            active: {
                story: false,
            }
        }
    },
    methods: {
        async renderStory(story) {
            utils.resetActiveStory()
            story.paragraphs.sort(utils.compareIDs)
            this.active.story = story
            await utils.sleep(.01)
                .then(timer => {
                    document.getElementById(`story-${story.id}`).classList.add('active')
                })
        },
    }
}

</script>