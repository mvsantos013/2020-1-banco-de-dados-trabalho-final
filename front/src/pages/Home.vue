<template>
  <div class="mt-5">
    <h1>Pacientes DEMO</h1>
    <v-data-table
      :headers="pacientesHeaders"
      :items="pacientes"
      :items-per-page="15"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
import axios from 'axios'

const API_PATH = 'https://ohup21d337.execute-api.us-east-1.amazonaws.com/dev/api'

export default {
  data(){
    return {
      pacientes: [],
      pacientesHeaders: [
        { text: 'ID Paciente', value: 'id_paciente'},
        { text: 'Sexo', value: 'ic_sexo'},
        { text: 'Ano Nascimento', value: 'aa_nascimento'},
        { text: 'País', value: 'cd_pais'},
        { text: 'UF', value: 'cd_uf'},
        { text: 'Município', value: 'cd_municipio'},
        { text: 'CEP Reduzido', value: 'cd_cepreduzido'},
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
        console.log('Error ao carregar pacientes.')
      }
    }
  }
}
</script>