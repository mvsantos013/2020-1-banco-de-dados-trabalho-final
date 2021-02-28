<template>
  <div class="mt-5">
    <h1 class="mb-3">Tipos de Atendimento</h1>
    <v-data-table
      :headers="headers"
      :items="tiposDeAtendimento"
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
      tiposDeAtendimento: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'nome', value: 'nome'},
      ]
    }
  },
  mounted(){
    if(this.tiposDeAtendimento.length == 0){
      this.fetchTiposDeAtendimento();
    }
  },
  methods:{
    async fetchTiposDeAtendimento(){
      try{
        const cache = localStorage.getItem('tiposDeAtendimento')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.tiposDeAtendimento = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/tipos-de-atendimento/`)
        this.tiposDeAtendimento = response.data

        // Caches data
        localStorage.setItem('tiposDeAtendimento', JSON.stringify(this.tiposDeAtendimento))
      } 
      catch(e){
        alert('Error ao carregar tiposDeAtendimento.')
      }
    }
  }
}
</script>