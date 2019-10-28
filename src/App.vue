<template>
  <div id="app">
    <ModuleView :content="courseware.topics[5].modules[0].content"/>
  </div>
</template>

<script>
import ModuleView from './components/ModuleView'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    ModuleView
  },
  data() {
    return {
      courseware: {}
    }
  },
  beforeMount() {
    axios.get("/state.json").then((response) => {
      this.courseware = response.data
    })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
