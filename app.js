Vue.createApp({
    delimiters: ['--', '--'],
    data() {
        return {
            title: 'Austen Myers',
            sub_title: 'Portfolio',
            pages: [
                {
                    id: 0,
                    title: 'About',
                    sections: []
                },
            ],
            active_page: {},
            active_section: ''
        }
    },
    methods: {
        async renderPage(page) {
            this.active_page = this.pages[page.id]
            this.active_section = ''
            let url = 'https://acmf-dev.herokuapp.com/api/'
            if (this.active_page.id === 0) {
                await fetch(url + 'stories')
                    .then(response => response.json())
                    .then(data => (this.active_page.sections = data.results))
            }
            console.log(this.active_page)
        },
        renderSection(section) {
            this.active_section = section
        }
    }

}).mount('#app')