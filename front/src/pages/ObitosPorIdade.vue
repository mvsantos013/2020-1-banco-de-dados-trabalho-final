<template>
  <div class="mt-5">
    <h1 class="mb-3">Óbitos por idade</h1>

    <pre class="query">
SELECT
CASE
WHEN T.Ano_Nascimento between 1930 and 1940 then 'Entre 80 e 90 anos'
WHEN T.Ano_Nascimento between 1941 and 1950 then 'Entre 70 e 80 anos'
WHEN T.Ano_Nascimento between 1951 and 1960 then 'Entre 60 e 70 anos'
WHEN T.Ano_Nascimento between 1961 and 1990 then 'Entre 30 e 60 anos'
WHEN T.Ano_Nascimento between 1991 and 2021 then 'Entre 0 e 30 anos'
END as faixas, SUM(T.Proporcao_Obito) as Proporcao_Obito FROM
   (SELECT
       PAC.aa_nascimento as Ano_Nascimento,
       COALESCE(T1.SOMA_ALTA / COUNT(*), 0) as Proporcao_Alta_Medica,
       COALESCE(T2.OBITO / COUNT(*), 0) as Proporcao_Obito,
       COALESCE(T3.SOMA_ADM / COUNT(*), 0) as Proporcao_Alta_Administrativa
   FROM
    pacientes as PAC
   INNER JOIN
     atendimentos AS ATD on ATD.id_paciente = PAC.id
   INNER JOIN
    desfechos AS DES on ATD.id = DES.id_atendimento
   INNER JOIN
     tipos_de_desfecho AS TIP on TIP.id = DES.id_tipo_desfecho
   LEFT JOIN
    (SELECT COUNT(*) AS SOMA_ADM, PAC.aa_nascimento as ANO FROM pacientes AS PAC inner join atendimentos as ATD on ATD.id_paciente = PAC.id INNER JOIN
        desfechos AS DES on DES.id_atendimento = ATD.id INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho like '%Alta administrativa%' GROUP BY PAC.aa_nascimento) as T3 on T3.ANO = PAC.aa_nascimento
   LEFT JOIN
    (SELECT COUNT(*) AS SOMA_ALTA, PAC.aa_nascimento as ANO FROM pacientes AS PAC inner join atendimentos as ATD on ATD.id_paciente = PAC.id INNER JOIN
        desfechos AS DES on DES.id_atendimento = ATD.id INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho in ('Alta médica melhorado', 'Alta médica curado') GROUP BY PAC.aa_nascimento) as T1 on T1.ANO = PAC.aa_nascimento
   LEFT JOIN
     (SELECT COUNT(*) AS OBITO, PAC.aa_nascimento as ANO FROM pacientes AS PAC inner join atendimentos as ATD on ATD.id_paciente = PAC.id INNER JOIN
        desfechos AS DES on DES.id_atendimento = ATD.id INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho like '%Óbito%' GROUP BY PAC.aa_nascimento) as T2 on T2.ANO = PAC.aa_nascimento
   GROUP BY
     PAC.aa_nascimento) as T
GROUP BY faixas
    </pre>

    <v-data-table
      :headers="headers"
      :items="obitosPorIdade"
      :items-per-page="15"
      class="elevation-1"
    >
      <!-- eslint-disable -->
      <!-- <template v-slot:item.Data="{ item }">
        <span>{{ new Date(item.Data).toLocaleString().slice(0,10) }}</span>
      </template> -->

      <template v-slot:item.Proporcao_Obito="{ item }">
        <span>{{ (item['Proporcao_Obito']*100).toFixed(2) }}</span>
      </template>
      <!-- eslint-enable -->
    </v-data-table>

    <div class="mt-10">
      <h3>Visualizações</h3>
      <div class="charts">
        <div style="width: 50%;">
          <h5 class="mb-3">Óbitos por idade</h5>
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
      obitosPorIdade: [],
      headers: [
        { text: 'Faixa etária', value: 'faixas'},
        { text: 'Proporção de óbitos (%)', value: 'Proporcao_Obito'},
      ],
    }
  },
  computed:{
    pieChartData(){
      return this.obitosPorIdade.map(item => [item.faixas, item.Proporcao_Obito])
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
        tooltip: { text: 'Proporção' }
      }
    }
  },
  mounted(){
    if(this.obitosPorIdade.length == 0){
      this.fetchObitosPorIdade();
    }
  },
  methods:{
    async fetchObitosPorIdade(){
      try{
        //const cache = localStorage.getItem('obitosPorIdade')

        // Get data from cache. Avoids overloading API.
        if(false){
          this.obitosPorIdade = JSON.parse(cache)
          return;
        }

        // Fetch data
        const response = await axios.get(`${API_PATH}/obitos-por-idade/`)
        this.obitosPorIdade = response.data
        this.obitosPorIdade = this.obitosPorIdade.map(x => ({...x, 'faixas': x.faixas ? x.faixas : 'Sem idade informada'}))

        // Caches data
        //localStorage.setItem('obitosPorIdade', JSON.stringify(this.obitosPorIdade))
      } 
      catch(e){
        console.log('Error ao carregar obitosPorIdade.')
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