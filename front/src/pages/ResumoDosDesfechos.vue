<template>
  <div class="mt-5">
    <h1 class="mb-3">Resumo dos desfechos</h1>

    <pre class="query">
SELECT 
  tipos_de_desfecho.desfecho as Desfecho, COUNT(*) as Quantidade  
FROM 
  atendimentos 
INNER JOIN 
  desfechos on atendimentos.id = desfechos.id_atendimento 
INNER JOIN 
  tipos_de_desfecho on tipos_de_desfecho.id = desfechos.id_tipo_desfecho 
GROUP BY 
  tipos_de_desfecho.desfecho
    </pre>

    <v-data-table
      :headers="headers"
      :items="desfechos"
      :items-per-page="15"
      class="elevation-1"
    ></v-data-table>

    <div class="mt-10">
      <h3>Visualizações</h3>
      <div class="charts">

        <div style="width: 50%;">
          <h5 class="mb-3">Proporção dos desfechos</h5>
          <PieChart
            :legends="['', '']"
            :chart-data="pieChartData"
            :chart-options="pieChartOptions"
          />
        </div>

        <div style="width: 50%;">
          <h5 class="mb-3">Proporção dos desfechos (Sem alta administrativa)</h5>
          <PieChart
            :legends="['', '']"
            :chart-data="pieChartData2"
            :chart-options="pieChartOptions"
          />
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import PieChart from '@/components/shared/charts/pie-chart.vue'

const API_PATH = process.env.VUE_APP_API_BASE_PATH

export default {
  components:{
    PieChart
  },
  data(){
    return {
      desfechos: [],
      headers: [
        { text: 'Desfecho', value: 'Desfecho'},
        { text: 'Quantidade', value: 'Quantidade'},
      ],
    }
  },
  computed:{
    pieChartData(){
      return this.desfechos.map(item => [item.Desfecho, item.Quantidade])
    },
    pieChartData2(){
      return this.desfechos.filter(item => item.Desfecho !== 'Alta Administrativa').map(item => [item.Desfecho, item.Quantidade])
    },
    pieChartOptions(){
      return {
        //pieHole: 0.35,
        //legend: { position: 'none', alignment: 'center' },
        width: '100%',
        height: '300',
        chartArea: { width: '85%', height: '95%' },
        colors: [
          '#79ff89',
          '#50e3c2',
          '#ffc935',
          '#51db84',
          '#8479ff',
          '#f28477',
          '#ed5555',
          '#854141',
          '#494f4c',
          '#058244',
          '#76a3d6',
          '#4323f6',
        ],
        tooltip: { text: 'Quantidade' }
      }
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
        const response = await axios.get(`${API_PATH}/desfechos-resumo/`)
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

<style lang="scss" scoped>
  .query{
    display: inline-block;
    background: rgba(0, 0, 0, 0.03);
    padding: 10px 20px 0 20px;
    margin-bottom: 20px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 0.9rem;
  }

  .charts{
    display: flex;
    margin-top: 2rem;
    margin-bottom: 15rem;
  }
</style>