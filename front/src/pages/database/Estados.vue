<template>
  <div class="mt-5">
    <h1 class="mb-3">Estados</h1>
    <v-data-table
      :headers="headers"
      :items="estados"
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
      estados: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'cd_uf', value: 'cd_uf'},
      ]
    }
  },
  mounted(){
    if(this.estados.length == 0){
      this.fetchEstados();
    }
  },
  methods:{
    async fetchEstados(){
      try{
        const cache = localStorage.getItem('estados')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.estados = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/estados/`)
        this.estados = response.data

        // Caches data
        localStorage.setItem('estados', JSON.stringify(this.estados))
      } 
      catch(e){
        alert('Error ao carregar estados.')
      }
    }
  }
}
</script>