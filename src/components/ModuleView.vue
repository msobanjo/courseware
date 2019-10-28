<template>
<div id="module-view" v-html="content"> </div>
</template>
<script>
       import Prism from 'prismjs'
export default {
   name: "ModuleView" ,
   props: {
       content: String
   },
   mounted() {
       Prism.highlightAll()
   }
}
</script>
<style scoped>

</style>
