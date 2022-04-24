<template>
    <div class="story">
        <h3 class="title">
            {{ story.title }}
        </h3>
        <div class="content">
            <div v-for="paragraph in story.paragraphs">
            <p v-if="paragraph.type === 'paragraph'">
                {{ paragraph.content }}
            </p>
            <ul v-if="paragraph.type === 'list'">
            {{ paragraph.content }}
            </ul>
            </div>
        </div>
    </div>
</template>

<script>


export default {
    name: 'Story',
    props: {
        story: Object,
    },

}

</script>