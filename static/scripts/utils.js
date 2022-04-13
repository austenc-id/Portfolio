export function compareIDs(a, b) {
    if (a.id < b.id) {
        return -1;
    }
    if (a.id > b.id) {
        return 1;
    }
    return 0;
}

export function sleep(sec) {
    let ms = sec * 1000
    return new Promise(resolve => setTimeout(resolve, ms));
}

export function resetActiveElements() {
    resetActiveStory()
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
}
export function resetActiveStory() {
    try {
        let sections = document.getElementById('stories')
        sections = sections.children
        for (let i = 0; i < sections.length; i++) {
            let element = sections[i]
            element.classList.remove('active')
        }
    }
    catch {
        console.log('no active section')
    }
}