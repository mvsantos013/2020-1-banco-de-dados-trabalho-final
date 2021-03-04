<template>
  <div class="mt-5">
    <h1>Relatório</h1>
    <v-container>
      <div class="relatorio">
        <div class="title">Introdução</div>
        <p>
          Coletamos os dados do HSL (Hospital Sírio Libanês), normalizamos e criamos uma infraestrutura de banco de dados a partir destes. Criamos uma aplicação do tipo cliente-servidor onde uma API consulta o banco de dados e oferece para a interface de usuário. Na interface há gráficos que ajudam a visualizar melhor os dados coletados.
        </p>
        <div class="title">Modelagem</div>
        <p>
          Começamos a modelagem do Banco de Dados a partir de três arquivos .csv 
          desnormalizados que podem ser acessados através do link que se encontra na área de referências. São eles: HSL_Desfechos_3, HSL_Exames_3, HSL_Pacientes_3. 
          A descrição dos arquivos pode ser lida através do link que está no tópico de referências.
        </p>
        
        <div class="title">Normalização</div>
        <p>
          Um dos primeiros arquivos analisados para a normalização foi o que mostrava os dados dos pacientes anonimizados. Percebemos que os dados dos campos IC_SEXO, CD_PAIS, CD_UF, CD_MUNICIPIO e CD_CEPREDUZIDO se repetiam com frequência e em alguns casos, havia poucos dados distintos, por exemplo em IC_SEXO, que apresentava apenas dois dados: “M” e “F”. Dessa forma, decidimos criar tabelas à parte para reduzir estas repetições e economizar espaço no banco. Além disso, em alguns casos, não foi possível normalizar perfeitamente pois haveria inconsistências. Foi o que aconteceu na tabela “enderecos” por exemplo, quando tentamos usar o campo CD_CEPREDUZIDO como chave estrangeira. Se isto fosse possível, não seria necessário usar como chaves estrangeiras os campos CD_UF e CD_MUNICIPIO,  já que cada CEP já se relaciona com esses dados. Contudo, como no dataset os CEP 's não estavam completos, utilizamos a abordagem comentada acima. 
        </p>

        <p>
          Também percebemos problemas na tabela “exames”, pois checamos que no dataset que apresentava os dados destes, nos campos DE_ANALITO e DE_VALOR_REFERENCIA havia inconsistências. Em alguns momentos, no campo DE_ANALITO há dois analitos sendo observados, enquanto no campo DE_VALOR_REFERENCIA não é especificado o valor de referência para cada um deles. Dessa forma, a informação é muito restrita a quem inseriu os dados, e não para quem consome, com isso, apenas separamos em uma tabela à parte os analitos analisados, enquanto os valores de referência não foram trabalhados diretamente, ou seja, colocados em uma tabela separada. Ao final de todo o processo de normalização, o trabalho final pode ser visto na imagem abaixo:
        </p>

        <p align="center">
          <img width="100%" src="https://raw.githubusercontent.com/mvsantos013/2020-1-banco-de-dados-trabalho-final/main/docs/imgs/db_logical_model.png">
        </p>

        <div class="title">Aplicação</div>
        <p>
          A aplicação usa arquitetura client-server, os respectivos códigos se encontram nas pastas front (client) e back (server).
        </p>
        <p>
          O backend hospedar o banco de dados e oferece uma API para o frontend, que por sua vez consumie a API e disponibilizar uma interface de usuário. 
          O backend foi escrito usando Python e o Serverless Framework, os serviços foram hospedados no AWS (Amazon Web Services) e no Hostgator. O frontend foi desenvolvido
          usando a linguagem Javascript e a framework VueJS. Abaixo há um diagrama da arquitetura da aplicação.
        </p>

        <p align="center">
          <img width="100%" src="https://raw.githubusercontent.com/mvsantos013/2020-1-banco-de-dados-trabalho-final/main/docs/imgs/architecture.png">
        </p>


        <div class="title">Conclusões</div>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum fringilla 
          consequat ante, at lacinia massa vestibulum non. Pellentesque habitant morbi tristique
          senectus et netus et malesuada fames ac turpis egestas. Aliquam erat volutpat. Phasellus
          quis libero sit amet turpis eleifend gravida nec quis risus. Donec varius, ligula et porttitor
          tristique, nibh nulla sodales nibh, mattis pellentesque erat turpis sit amet eros.
          Donec tempus, purus ut luctus pellentesque, lacus nunc accumsan augue, eget egestas lectus augue
          id augue. Vivamus sit amet volutpat nisl. Cras ac mattis lectus. Cras cursus augue tortor, volutpat
          dignissim leo ultrices ac. Nam non nunc justo. Suspendisse potenti. Nulla scelerisque turpis mollis
          bibendum consectetur. Fusce venenatis tempor tempor.
        </p>

        <p class="mt-10">
          Código-fonte: 
          <a href=" https://github.com/mvsantos013/2020-1-banco-de-dados-trabalho-final" target="_blank">
            https://github.com/mvsantos013/2020-1-banco-de-dados-trabalho-final
          </a>
        </p>
      </div>
    </v-container>
  </div>
</template>

<style lang="scss" scoped>
.relatorio{
  background: rgb(249, 249, 249);
  border-radius: 6px;
  max-width: 50rem;
  margin: auto;
  padding: 2rem;

  .title{
    border-bottom: solid 1px rgba(0,0,0,0.05);
    margin-bottom: 0.5rem;

    &:not(:first-child){
      margin-top: 1.5rem;
    }
  }

  p{
    margin-bottom: 0.5rem;
    color: #707070;
  }
}
</style>