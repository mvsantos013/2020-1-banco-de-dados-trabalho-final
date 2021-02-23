<template>
  <div class="mt-5">
    <h1 class="mb-3">Unidades</h1>
    <v-data-table
      :headers="headers"
      :items="unidades"
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
      unidades: [],
      headers: [
        { text: 'id_unidade', value: 'id_unidade'},
        { text: 'sexo', value: 'sexo'},
      ]
    }
  },
  mounted(){
    if(this.unidades.length == 0){
      this.fetchUnidades();
    }
  },
  methods:{
    async fetchUnidades(){
      try{
        const cache = localStorage.getItem('unidades')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.unidades = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/unidades/`)
        this.unidades = response.data

        // Caches data
        localStorage.setItem('unidades', JSON.stringify(this.unidades))
      } 
      catch(e){
        console.log('Error ao carregar unidades.')
      }
    }
  }
}
</script>