class Collector {
    async fetchContent(url){
        let links = []
        let chapters = []
        await this.fetchURL(url + '/links')
            .then(data => (links = data.results))
        await this.fetchURL(url + '/chapters')
            .then(data => (chapters = data.results))
        await this.fetchDetails(chapters)
            .then(data => (chapters = data))
            .catch(error => console.log(error))
        return { links: links, chapters: chapters }
    }
    async fetchDetails(chapters){
        chapters.forEach(chapter => {
            let stories = []
            chapter.stories.forEach(story => {
                this.fetchURL(story)
                    .then(sdata => {
                        let paragraphs = []
                        sdata.paragraphs.forEach(paragraph => {
                            this.fetchURL(paragraph)
                                .then(pdata => paragraphs.push(pdata))
                        })
                        sdata.paragraphs = paragraphs
                        return sdata
                    })
                    .then(data => stories.push(data))
            })
            chapter.stories = stories
        })
        return chapters
    }
    async fetchURL(url){
        let data = await fetch(url)
            .then(response => response.json())
            // .then(data => {return data})
            .catch(error => console.log(error))
        return data
    }
}

export const collector = new Collector()