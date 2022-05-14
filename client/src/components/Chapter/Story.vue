<template>
    <div class="story">
        <h3 class="title">
            {{ active.story.title }}
        </h3>
        <div class="content">
            <p v-for="paragraph in active.story.paragraphs">
                {{ paragraph.content }}
            </p>
        </div>
    </div>
</template>

<script>


export default {
    name: 'Story',
    data(){
        return this.$store.state
    }

}

</script>