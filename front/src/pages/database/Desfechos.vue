<template>
  <div class="mt-5">
    <h1 class="mb-3">Desfechos</h1>
    <v-data-table
      :headers="headers"
      :items="desfechos"
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
      desfechos: [],
      headers: [
        { text: 'id_paciente', value: 'id_paciente'},
        { text: 'id_atendimento', value: 'id_atendimento'},
        { text: 'id_clinica', value: 'id_clinica'},
        { text: 'dt_desfecho', value: 'dt_desfecho'},
        { text: 'id_tipo_desfecho', value: 'id_tipo_desfecho'},
      ]
    }
  },
  mounted(){
    if(this.desfechos.length == 0){
      this.fetchDesfechos();
    }
  },
  methods:{
    async fetchDesfechos(){
      try{
        const cache = localStorage.getItem('desfechos')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.desfechos = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/desfechos/`)
        this.desfechos = response.data

        // Caches data
        localStorage.setItem('desfechos', JSON.stringify(this.desfechos))
      } 
      catch(e){
        console.log('Error ao carregar desfechos.')
      }
    }
  }
}
</script>