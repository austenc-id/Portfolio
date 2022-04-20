class Utils{
    sleep(sec) {
        let ms = sec * 1000
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    resetActiveElements() {
        this.resetActiveStory()
        let active_elements = document.getElementsByClassName('active')
        try {
            for (let i = 0; i < active_elements.length; i++) {
                let element = active_elements[i]
                element.classList.remove('active')
            }
        }
        catch {
        }
    }
    resetActiveStory() {
        try {
            let stories = document.getElementsByClassName('story')
            for (let i = 0; i < stories.length; i++) {
                let element = stories[i]
                element.classList.remove('active')
            }
        }
        catch {
        }
    }
    compareIDs(a, b) {
        if (a.id < b.id) {
            return -1;
        }
        if (a.id > b.id) {
            return 1;
        }
        return 0;
    }
}

export const utils = new Utils()