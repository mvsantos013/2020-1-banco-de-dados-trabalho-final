<template>
  <div class="mt-5">
    <h1 class="mb-3">Sexos</h1>
    <v-data-table
      :headers="headers"
      :items="sexos"
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
      sexos: [],
      headers: [
        { text: 'ID', value: 'id'},
        { text: 'Sexo', value: 'sexo'},
      ]
    }
  },
  mounted(){
    if(this.sexos.length == 0){
      this.fetchSexos();
    }
  },
  methods:{
    async fetchSexos(){
      try{
        const cache = localStorage.getItem('sexos')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.sexos = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/sexos/`)
        this.sexos = response.data

        // Caches data
        localStorage.setItem('sexos', JSON.stringify(this.sexos))
      } 
      catch(e){
        console.log('Error ao carregar sexos.')
      }
    }
  }
}
</script>