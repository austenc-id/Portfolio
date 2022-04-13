import { fetchContent } from "./scripts/courier.js";
import { sleep, compareIDs, resetActiveElements, resetActiveStory } from "./scripts/utils.js"


Vue.createApp({
    data() {
        return {
            title: 'Austen Myers',
            sub_title: 'Demo',
            load_time: '(may take up to 10 seconds)',
            loading: 'Waking up Heroku Dyno...',
            links: [],
            chapters: [],
            active: {
                chapter: {},
                story: {}
            },
        }
    },
    created() {
        this.collectData()
    },
    mounted() {
    },
    delimiters: ['--', '--'],
    methods: {

        async collectData() {
            await fetchContent()
                .then(data => (
                    this.loading = 'Loading...',
                    this.load_time = 2,
                    this.links = data.links,
                    this.chapters = data.chapters
                ))
            for (let i = this.load_time; i > 0; i--) {
                await sleep(1)
                    .then(data => (console.log(this.load_time, i)))
                    .then(data => (this.load_time--))
                    .then(data => {
                        if (this.load_time === 0) {
                            this.loading = false
                            this.renderChapter(this.chapters[0])
                        }
                    })
            }
        },

        async renderChapter(chapter) {
            chapter.stories.sort(compareIDs)
            this.active.chapter = this.chapters[chapter.id - 1]
            this.active.story = {}
            resetActiveElements()
            await this.renderStory(this.active.chapter.stories[0])
            document.getElementById(`chapter-${chapter.id}`).classList.add('active')
        },

        async renderStory(story) {
            resetActiveStory()
            story.paragraphs.sort(compareIDs)
            this.active.story = story
            await sleep(.01)
                .then(promise => { document.getElementById(`story-${story.id}`).classList.add('active') })
        },
    }
}).mount('#app')