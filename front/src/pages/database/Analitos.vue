<template>
  <div class="mt-5">
    <h1 class="mb-3">Analitos</h1>
    <v-data-table
      :headers="headers"
      :items="analitos"
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
      analitos: [],
      headers: [
        { text: 'id_analito', value: 'id_analito'},
        { text: 'nome', value: 'nome'},
      ]
    }
  },
  mounted(){
    if(this.analitos.length == 0){
      this.fetchAnalitos();
    }
  },
  methods:{
    async fetchAnalitos(){
      try{
        const cache = localStorage.getItem('analitos')

        // Get data from cache. Avoids overloading API.
        if(false){
          this.analitos = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/analitos/`)
        this.analitos = response.data

        // Caches data
        localStorage.setItem('analitos', JSON.stringify(this.analitos))
      } 
      catch(e){
        console.log(e)
        alert('Error ao carregar analitos.')
      }
    }
  }
}
</script>