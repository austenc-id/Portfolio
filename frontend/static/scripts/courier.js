export async function fetchContent() {
    const base_url = 'https://acmf-dev.herokuapp.com/api'
    let links = []
    let chapters = []
    await fetchURL(base_url + '/links')
        .then(data => (links = data.results))
    await fetchURL(base_url + '/chapters')
        .then(data => (chapters = data.results))
    await fetchDetails(chapters)
        .then(data => (chapters = data))
        .catch(error => console.log(error))
    return { links: links, chapters: chapters }
}
export async function fetchDetails(chapters) {
    chapters.forEach(chapter => {
        let stories = []
        chapter.stories.forEach(story => {
            fetchURL(story)
                .then(sdata => {
                    let paragraphs = []
                    sdata.paragraphs.forEach(paragraph => {
                        fetchURL(paragraph)
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
export async function fetchURL(url) {
    let data = await fetch(url)
        .then(response => response.json())
        .catch(error => console.log(error))
    return data
}