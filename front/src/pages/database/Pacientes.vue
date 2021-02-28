<template>
  <div class="mt-5">
    <h1 class="mb-3">Pacientes</h1>
    <v-data-table
      :headers="headers"
      :items="pacientes"
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
      pacientes: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'id_sexo', value: 'id_sexo'},
        { text: 'aa_nascimento', value: 'aa_nascimento'},
        { text: 'id_endereco', value: 'id_endereco'},
      ]
    }
  },
  mounted(){
    if(this.pacientes.length == 0){
      this.fetchPacientes();
    }
  },
  methods:{
    async fetchPacientes(){
      try{
        const cache = localStorage.getItem('pacientes')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.pacientes = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/pacientes/`)
        this.pacientes = response.data

        // Caches data
        localStorage.setItem('pacientes', JSON.stringify(this.pacientes))
      } 
      catch(e){
        alert('Error ao carregar pacientes.')
      }
    }
  }
}
</script>