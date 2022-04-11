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
                // {
                //     id: 1,
                //     title: 'Test',
                //     sections: []
                // },
            ],
            active_page: {},
            active_section: ''
        }
    },
    methods: {
        async renderPage(page) {
            this.active_page = this.pages[page.id]
            this.pages.forEach(page => {
                document.getElementById(`nav-link-${page.id}`).classList.remove('active')
            })
            document.getElementById(`nav-link-${page.id}`).classList.add('active')
            if (this.active_page.id === 0) {
                await fetch('https://acmf-dev.herokuapp.com/api/stories')
                    .then(response => response.json())
                    .then(data => (this.active_page.sections = data.results))
            }


        },
        renderSection(section) {
            this.active_section = section
            this.active_page.sections.forEach(section => {
                console.log(section.label)
                document.getElementById(`page-nav-${section.label}`).classList.remove('active')
            })
            document.getElementById(`page-nav-${section.label}`).classList.add('active')
        },
    }

}).mount('#app')