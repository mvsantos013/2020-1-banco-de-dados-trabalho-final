<template>
  <div class="mt-5">
    <h1 class="mb-3">Locais De Exame</h1>
    <v-data-table
      :headers="headers"
      :items="locaisDeExame"
      :items-per-page="15"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import axios from 'axios'

const API_PATH = process.env.VUE_APP_API_BASE_PATH

export default {
  data(){
    return {
      locaisDeExame: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'nome', value: 'nome'},
      ]
    }
  },
  mounted(){
    if(this.locaisDeExame.length == 0){
      this.fetchLocaisDeExame();
    }
  },
  methods:{
    async fetchLocaisDeExame(){
      try{
        const cache = localStorage.getItem('locaisDeExame')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.locaisDeExame = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/locais-de-exame/`)
        this.locaisDeExame = response.data

        // Caches data
        localStorage.setItem('locaisDeExame', JSON.stringify(this.locaisDeExame))
      } 
      catch(e){
        console.log('Error ao carregar locaisDeExame.')
      }
    }
  }
}
</script>