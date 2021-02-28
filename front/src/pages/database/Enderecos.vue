<template>
  <div class="mt-5">
    <h1 class="mb-3">Endereços</h1>
    <v-data-table
      :headers="headers"
      :items="enderecos"
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
      enderecos: [],
      headers: [
        { text: 'id', value: 'id'},
        { text: 'id_pais', value: 'id_pais'},
        { text: 'id_uf', value: 'id_uf'},
        { text: 'id_municipio', value: 'id_municipio'},
        { text: 'cd_cepreduzido', value: 'cd_cepreduzido'},
      ]
    }
  },
  mounted(){
    if(this.enderecos.length == 0){
      this.fetchEnderecos();
    }
  },
  methods:{
    async fetchEnderecos(){
      try{
        const cache = localStorage.getItem('enderecos')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.enderecos = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/enderecos/`)
        this.enderecos = response.data

        // Caches data
        localStorage.setItem('enderecos', JSON.stringify(this.enderecos))
      } 
      catch(e){
        alert('Error ao carregar enderecos.')
      }
    }
  }
}
</script>