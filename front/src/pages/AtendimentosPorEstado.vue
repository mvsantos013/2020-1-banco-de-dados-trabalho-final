<template>
  <div class="mt-5">
    <h1 class="mb-3">Atendimentos por estado</h1>

    <pre class="query">
SELECT 
  EST.cd_uf as Estado,
        COUNT(*) as Quantidade_de_Atendimentos
FROM
  estados as EST
INNER JOIN
  enderecos as ENDE on ENDE.id_uf = EST.id
INNER JOIN
  pacientes as PAC on PAC.id_endereco = ENDE.id
INNER JOIN
  atendimentos as AT on AT.id_paciente = PAC.id
INNER JOIN
  desfechos as DES on DES.id_atendimento = AT.id
INNER JOIN
  tipos_de_desfecho as TIP on TIP.id = DES.id_tipo_desfecho
GROUP BY
  EST.cd_uf
    </pre>

    <v-data-table
      :headers="headers"
      :items="atendimentosPorEstado"
      :items-per-page="15"
      class="elevation-1"
    >
      <!-- eslint-disable -->
      <!-- <template v-slot:item.Data="{ item }">
        <span>{{ new Date(item.Data).toLocaleString().slice(0,10) }}</span>
      </template>

      <template v-slot:item.Proporção_de_Alta_Administrativa="{ item }">
        <span>{{ (item['Proporção_de_Alta_Administrativa']*100).toFixed(2) }}</span>
      </template> -->
      <!-- eslint-enable -->
    </v-data-table>

    <div class="mt-10">
      <h3>Visualizações</h3>
      <div class="charts">
        <div style="width: 50%;">
          <h5 class="mb-3">Atendimentos por estado</h5>
          <PieChart
            :legends="['', '']"
            :chart-data="pieChartData"
            :chart-options="pieChartOptions"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import LineChart from '@/components/shared/charts/line-chart.vue'
import PieChart from '@/components/shared/charts/pie-chart.vue'

const API_PATH = process.env.VUE_APP_API_BASE_PATH

export default {
  components:{
    PieChart,
    LineChart
  },
  data(){
    return {
      atendimentosPorEstado: [],
      headers: [
        { text: 'Estado', value: 'Estado'},
        { text: 'Quantidade de Atendimentos', value: 'Quantidade_de_Atendimentos'},
      ],
    }
  },
  computed:{
    pieChartData(){
      return this.atendimentosPorEstado.map(item => [item.Estado, item.Quantidade_de_Atendimentos])
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
    if(this.atendimentosPorEstado.length == 0){
      this.fetchAtendimentosPorEstado();
    }
  },
  methods:{
    async fetchAtendimentosPorEstado(){
      try{
        //const cache = localStorage.getItem('atendimentosPorEstado')

        // Get data from cache. Avoids overloading API.
        if(false){
          this.atendimentosPorEstado = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/atendimentos-por-estado/`)
        this.atendimentosPorEstado = response.data

        // Caches data
        //localStorage.setItem('atendimentosPorEstado', JSON.stringify(this.atendimentosPorEstado))
      } 
      catch(e){
        console.log('Error ao carregar atendimentosPorEstado.')
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