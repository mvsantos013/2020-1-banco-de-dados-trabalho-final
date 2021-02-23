<template>
  <div class="mt-5">
    <h1 class="mb-3">Tipos de Desfecho</h1>
    <v-data-table
      :headers="headers"
      :items="tiposDeDesfecho"
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
      tiposDeDesfecho: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'desfecho', value: 'desfecho'},
      ]
    }
  },
  mounted(){
    if(this.tiposDeDesfecho.length == 0){
      this.fetchTiposDeDesfecho();
    }
  },
  methods:{
    async fetchTiposDeDesfecho(){
      try{
        const cache = localStorage.getItem('tiposDeDesfecho')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.tiposDeDesfecho = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/tipos-de-desfecho/`)
        this.tiposDeDesfecho = response.data

        // Caches data
        localStorage.setItem('tiposDeDesfecho', JSON.stringify(this.tiposDeDesfecho))
      } 
      catch(e){
        console.log('Error ao carregar tiposDeDesfecho.')
      }
    }
  }
}
</script>