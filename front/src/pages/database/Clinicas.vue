<template>
  <div class="mt-5">
    <h1 class="mb-3">Clínicas</h1>
    <v-data-table
      :headers="headers"
      :items="clinicas"
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
      clinicas: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'nome', value: 'nome'},
      ]
    }
  },
  mounted(){
    if(this.clinicas.length == 0){
      this.fetchClinicas();
    }
  },
  methods:{
    async fetchClinicas(){
      try{
        const cache = localStorage.getItem('clinicas')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.clinicas = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/clinicas/`)
        this.clinicas = response.data

        // Caches data
        localStorage.setItem('analitos', JSON.stringify(this.analitos))
      } 
      catch(e){
        alert('Error ao carregar analitos.')
      }
    }
  }
}
</script>