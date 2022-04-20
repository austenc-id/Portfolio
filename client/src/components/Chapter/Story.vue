<template>
    <div class="story">
        <h3 class="title">
            {{ story.title }}
        </h3>
        <div class="content">
            <p v-for="paragraph in story.paragraphs">
                {{ paragraph.content }}
            </p>
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