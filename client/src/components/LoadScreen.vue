<template>
    <main class="load-screen">
        <h1 class="message">
            {{ message }}
        </h1>
        <h2 class="timer">
            {{ time }}
        </h2>
    </main>
</template>

<script>
export default {
    name: 'LoadScreen',
    props: {
        message: String,
        time: [String, Number],
    }
  }
</script>
