<template>
  <div class="mt-5">
    <h1 class="mb-3">Atendimentos</h1>
    <v-data-table
      :headers="headers"
      :items="atendimentos"
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
      atendimentos: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'dt_atendimento', value: 'dt_atendimento'},
        { text: 'id_tipo_atendimento', value: 'id_tipo_atendimento'},
        { text: 'id_paciente', value: 'id_paciente'},
      ]
    }
  },
  mounted(){
    if(this.atendimentos.length == 0){
      this.fetchAtendimentos();
    }
  },
  methods:{
    async fetchAtendimentos(){
      try{
        const cache = localStorage.getItem('atendimentos')

        // Get data from cache. Avoids overloading API.
        if(false){
          this.atendimentos = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/atendimentos/`)
        this.atendimentos = response.data

        // Caches data
        localStorage.setItem('atendimentos', JSON.stringify(this.atendimentos))
      } 
      catch(e){
        console.log('Error ao carregar atendimentos.')
      }
    }
  }
}
</script>