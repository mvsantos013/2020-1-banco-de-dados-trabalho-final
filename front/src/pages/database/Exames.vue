<template>
  <div class="mt-5">
    <h1 class="mb-3">Exames</h1>
    <v-data-table
      :headers="headers"
      :items="exames"
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
      exames: [],
      headers: [
        { text: 'id_exame', value: 'id_exame'},
        { text: 'id_atendimento', value: 'id_atendimento'},
        { text: 'dt_coleta', value: 'dt_coleta'},
        { text: 'id_local_exame', value: 'id_local_exame'},
        { text: 'id_tipo_exame', value: 'id_tipo_exame'},
        { text: 'id_analito', value: 'id_analito'},
        { text: 'de_resultado', value: 'de_resultado'},
        { text: 'id_unidade', value: 'id_unidade'},
        { text: 'de_valor_referencia', value: 'de_valor_referencia'},
      ]
    }
  },
  mounted(){
    if(this.exames.length == 0){
      this.fetchExames();
    }
  },
  methods:{
    async fetchExames(){
      try{
        //const cache = localStorage.getItem('exames')

        // Get data from cache. Avoids overloading API.
        if(false){
          this.exames = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/exames/`)
        this.exames = response.data

        // Caches data
        //localStorage.setItem('exames', JSON.stringify(this.exames))
      } 
      catch(e){
        alert('Error ao carregar exames.')
      }
    }
  }
}
</script>