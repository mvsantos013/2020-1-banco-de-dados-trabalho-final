<template>
  <div class="mt-5">
    <h1 class="mb-3">Municípios</h1>
    <v-data-table
      :headers="headers"
      :items="municipios"
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
      municipios: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'cd_municipio', value: 'cd_municipio'},
      ]
    }
  },
  mounted(){
    if(this.municipios.length == 0){
      this.fetchMunicipios();
    }
  },
  methods:{
    async fetchMunicipios(){
      try{
        const cache = localStorage.getItem('municipios')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.municipios = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/municipios/`)
        this.municipios = response.data

        // Caches data
        localStorage.setItem('municipios', JSON.stringify(this.municipios))
      } 
      catch(e){
        console.log('Error ao carregar municipios.')
      }
    }
  }
}
</script>