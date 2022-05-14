<template>
    <main class="load-screen">
        <h1 class="message">
            {{ loading.message }}
        </h1>
        <h2 class="timer">
            {{ loading.time }}
        </h2>
    </main>
</template>

<script>
export default {
    name: 'LoadScreen',
    data(){
        return this.$store.state
    }
  }
</script>
