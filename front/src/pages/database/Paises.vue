<template>
  <div class="mt-5">
    <h1 class="mb-3">Países</h1>
    <v-data-table
      :headers="headers"
      :items="paises"
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
      paises: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'cd_pais', value: 'cd_pais'},
      ]
    }
  },
  mounted(){
    if(this.paises.length == 0){
      this.fetchPaises();
    }
  },
  methods:{
    async fetchPaises(){
      try{
        const cache = localStorage.getItem('paises')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.paises = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/paises/`)
        this.paises = response.data

        // Caches data
        localStorage.setItem('paises', JSON.stringify(this.paises))
      } 
      catch(e){
        alert('Error ao carregar paises.')
      }
    }
  }
}
</script>