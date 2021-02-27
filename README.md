# 2020-1-banco-de-dados-trabalho-final

Trabalho final da disciplina Banco de Dados I durante o período letivo 2020.1

Análise e visualização dos [dados](https://repositoriodatasharingfapesp.uspdigital.usp.br/handle/item/97) do Hospital Sírio Libanês (HSL).

## Arquitetura

A aplicação usa arquitetura client-server, os respectivos códigos se encontram nas pastas front (client) e back (server).

<p align="center">
  <img width="100%" src="https://github.com/mvsantos013/2020-1-banco-de-dados-trabalho-final/blob/main/docs/imgs/architecture.png">
</p>

## Backend

Serviço: Hospedar o banco de dados e oferecer uma API para o frontend.

Linguagem: Javascript e Serverless Framework

Infraestrutura: AWS (API Gateway + Lambda functions + MySQL )


## Frontend

Serviço: Consumir a API e disponibilizar uma interface de usuário.

Linguagem: Javascript e VueJS

Infraestrutura: AWS (S3)


## Aplicativo WEB

A aplicação se encontra online em: http://bd-2020-1-trabalho-final.s3-website-us-east-1.amazonaws.com/

Mais instruções sobre como rodar localmente se encontram nas pastas back e front.
