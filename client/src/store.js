export const Production = {
  state() {
    return {
      urls: {
        base: "https://acmf-dev.herokuapp.com/api",
        links: "https://acmf-dev.herokuapp.com/api/links",
        chapters: "https://acmf-dev.herokuapp.com/api/chapters",
      },
    };
  },
  mutations: {},
};

export const Development = {
  state() {
    return {
      urls: {
        base: "http://localhost:8000/api",
        links: "http://localhost:8000/api/links",
        chapters: "http://localhost:8000/api/chapters",
      },
      active: {
        loadScreen: true,
        header: false,
        navbar: false,
        chapter: false,
        story: false,
      },
      loading: {
        message: "Waking up Heroku Dyno...",
        time: "(may take up to 10 seconds)",
      },
      titles: {
        title: "Austen Myers",
        subTitle: "Demo",
      },
      links: [],
      chapters: [],
      key: 0,
    };
  },
  getters: {},
  actions: {
    async fetchLinks(context) {
      context.dispatch("fetchContent", context.state.urls.links).then((links) => {
        return context.commit("setLinks", links.results);
      });
    },
    async fetchChapters(context) {
      context.dispatch("fetchContent", context.state.urls.chapters)
        .then((chapters) => chapters.results)
        .then((chapters) => {
          chapters.forEach((chapter) => {
            let urls = chapter.stories;
            chapter.stories = [];
            urls.forEach((url) => {
              fetch(url)
                .then((story) => story.json())
                .then((story) => {
                  let paragraphUrls = story.paragraphs;
                  story.paragraphs = [];
                  paragraphUrls.forEach(url => {
                    fetch(url)
                    .then((paragraph) => paragraph.json())
                    .then((paragraph) => {
                      story.paragraphs.push(paragraph);
                    });
                  })
                  return story
                })
                .then((story) => {
                  chapter.stories.push(story);
                });
            });
          });
          return chapters;
        })
        .then((chapters) => {
          context.commit("setChapters", chapters);
        });
    },
    async fetchContent(context, url) {
      let content = await fetch(url)
        .then((content) => content.json());
      return content;
    },

  },
  mutations: {
    setLinks(state, links) {
      state.links = links;
      //   console.log(state.links);
    },
    setChapters(state, chapters) {
      //   console.log(chapters);
      state.chapters = chapters;
        // console.log(state.chapters);
    },
  },
};
