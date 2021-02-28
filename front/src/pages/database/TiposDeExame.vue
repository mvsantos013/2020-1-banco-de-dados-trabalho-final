<template>
  <div class="mt-5">
    <h1 class="mb-3">Tipos de Exame</h1>
    <v-data-table
      :headers="headers"
      :items="tiposDeExame"
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
      tiposDeExame: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'nome', value: 'nome'},
      ]
    }
  },
  mounted(){
    if(this.tiposDeExame.length == 0){
      this.fetchTiposDeExame();
    }
  },
  methods:{
    async fetchTiposDeExame(){
      try{
        const cache = localStorage.getItem('tiposDeExame')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.tiposDeExame = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/tipos-de-exame/`)
        this.tiposDeExame = response.data

        // Caches data
        localStorage.setItem('tiposDeExame', JSON.stringify(this.tiposDeExame))
      } 
      catch(e){
        alert('Error ao carregar tiposDeExame.')
      }
    }
  }
}
</script>