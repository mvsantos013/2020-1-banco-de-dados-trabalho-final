<template>
  <div class="mt-5">
    <h1 class="mb-3">Altas Administrativas</h1>

    <pre class="query">
SELECT 
  DES.dt_desfecho as Data, 
  SOMA_ADM / COUNT(*) as Proporção_de_Alta_Administrativa
FROM 
  atendimentos AS ATD
INNER JOIN 
  desfechos AS DES on ATD.id = DES.id_atendimento
INNER JOIN
  tipos_de_desfecho AS TIP on TIP.id = DES.id_tipo_desfecho
INNER JOIN
  (SELECT 
    COUNT(*) AS SOMA_ADM, DES.dt_desfecho
  FROM 
    desfechos AS DES
  INNER JOIN
    tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho
  WHERE 
    TIP.desfecho like '%Administrativa%' 
  GROUP BY 
    DES.dt_desfecho) as T on T.dt_desfecho = DES.dt_desfecho
GROUP BY
  DES.dt_desfecho
    </pre>

    <v-data-table
      :headers="headers"
      :items="altasAdministrativas"
      :items-per-page="15"
      class="elevation-1"
    >
      <!-- eslint-disable -->
      <template v-slot:item.Data="{ item }">
        <span>{{ new Date(item.Data).toLocaleString().slice(0,10) }}</span>
      </template>

      <template v-slot:item.Proporção_de_Alta_Administrativa="{ item }">
        <span>{{ (item['Proporção_de_Alta_Administrativa']*100).toFixed(2) }}</span>
      </template>
      <!-- eslint-enable -->
    </v-data-table>

    <div class="mt-10">
      <h3>Visualizações</h3>
      <div class="charts">
        <div style="width: 100%">
          <LineChart
          v-if="Array.isArray(chartData)"
          :legends="['Data', 'Proporção de Alta Administrativa']"
          :chartData="chartData"
          :chartOptions="chartOptions"
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
      altasAdministrativas: [],
      headers: [
        { text: 'Data', value: 'Data'},
        { text: 'Proporção de Alta Administrativa (%)', value: 'Proporção_de_Alta_Administrativa'},
      ],
    }
  },
  computed:{
    chartData(){
      const data = this.altasAdministrativas.map(item => 
        [new Date(item.Data).toLocaleString().slice(0,10), item['Proporção_de_Alta_Administrativa']]
      )
      return JSON.parse(JSON.stringify(data))
    },
    chartOptions(){
      const baseColor = '#999'
      const width = 82
      return {
        curveType: 'function',
        legend: { position: 'bottom', textStyle: { color: baseColor } },
        chartArea: { top: 10, width: `${width}%`, height: '80%' },
        height: 450,
        hAxis: {
          format: 'dd/MMM/yyyy',
          gridlines: { color: '#edf2f5', count: 4 },
          textStyle: { color: baseColor },
          titleTextStyle: { color: baseColor }
        },
        vAxis: {
          title: 'Proporção',
          //format: 'R$ #,###.##',
          gridlines: { color: '#edf2f5', count: 4 },
          textStyle: { color: baseColor, fontSize: 12 },
          titleTextStyle: { color: baseColor, italic: false },
          logScale: false
        },
        explorer: { actions: ['dragToZoom', 'rightClickToReset'] },
        colors: ['#4a90e2', '#4a90e2'],
        baselineColor: 'transparent'
      }
    }
  },
  mounted(){
    if(this.altasAdministrativas.length == 0){
      this.fetchAltasAdministrativas();
    }
  },
  methods:{
    async fetchAltasAdministrativas(){
      try{
        const cache = localStorage.getItem('altasAdministrativas')

        // Get data from cache. Avoids overloading API.
        if(cache){
          this.altasAdministrativas = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/altas-administrativas/`)
        this.altasAdministrativas = response.data

        // Caches data
        localStorage.setItem('altasAdministrativas', JSON.stringify(this.altasAdministrativas))
      } 
      catch(e){
        console.log('Error ao carregar altasAdministrativas.')
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