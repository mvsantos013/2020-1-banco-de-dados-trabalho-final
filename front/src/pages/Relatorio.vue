<template>
  <div class="mt-5">
    <h1>Relatório</h1>
    <v-container>
      <div class="relatorio">
        <div class="title">Introdução</div>
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
        
        <div class="title">Normalização</div>
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