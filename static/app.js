Vue.createApp({
    delimiters: ['--', '--'],
    data() {
        return {
            title: 'Austen Myers',
            sub_title: 'Demo',
            links: [],
            pages: [
                {
                    id: 0,
                    label: '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6zm5-.793V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/><path fill-rule="evenodd" d="M7.293 1.5a1 1 0 0 1 1.414 0l6.647 6.646a.5.5 0 0 1-.708.708L8 2.207 1.354 8.854a.5.5 0 1 1-.708-.708L7.293 1.5z"/></svg>',
                    count: 0,
                    sections: []
                },
                {
                    id: 1,
                    label: 'About Me',
                    count: 0,
                    sections: []
                },
                {
                    id: 2,
                    label: 'Patrons',
                    count: 0,
                    sections: []
                },
            ],
            active_page: {},
            active_section: '',
        }
    },
    created() {
        this.fetchLinks()
        this.fetchStories()
    },
    mounted() {
        this.renderPage(this.pages[0])
    },
    methods: {
        async fetchLinks() {
            await fetch('https://acmf-dev.herokuapp.com/api/links')
                .then(response => response.json())
                .then(data => (this.links = data.results))
        },
        async fetchStories() {
            await fetch('https://acmf-dev.herokuapp.com/api/stories')
                .then(response => response.json())
                .then(data => {
                    let stories = data.results.sort(this.compareIDs)
                    stories.forEach(story => {
                        let paragraphs = []
                        story.paragraphs.forEach(url => {
                            this.fetchParagraph(url)
                                .then(data => paragraphs.push(data))
                        })
                        story.paragraphs = paragraphs.sort(this.compareIDs)
                        let page = story.page_index
                        this.pages[page].sections.push(story)
                        this.pages[page].count++
                    })
                })

        },
        async fetchParagraph(url) {
            let data = await fetch(url)
                .then(response => response.json())
            return data
        },
        renderPage(page) {
            this.active_page = this.pages[page.id]
            this.resetActiveElements()
            document.getElementById(`nav-link-${page.id}`).classList.add('active')
        },
        renderSection(section) {
            this.resetActiveSection()
            this.active_section = section
            document.getElementById(`page-nav-${section.id}`).classList.add('active')
        },
        compareIDs(a, b) {
            if (a.id < b.id) {
                return -1;
            }
            if (a.id > b.id) {
                return 1;
            }
            return 0;
        },
        resetActiveElements() {
            this.resetActiveSection()
            let active_elements = document.getElementsByClassName('active')
            try {
                for (let i = 0; i < active_elements.length; i++) {
                    let element = active_elements[i]
                    element.classList.remove('active')
                }
            }
            catch {
                console.log('no active elements')
            }
        },
        resetActiveSection() {
            try {
                let sections = document.getElementById('page-nav')
                sections = sections.children
                for (let i = 0; i < sections.length; i++) {
                    let element = sections[i]
                    element.classList.remove('active')
                }
            }
            catch {
                console.log('no active section')
            }
            this.active_section = ''
        }
    }

}).mount('#app')