# 2020-1-banco-de-dados-trabalho-final

Trabalho final da disciplina Banco de Dados I durante o período letivo 2020.1

## Arquitetura

A aplicação usa arquitetura client-server, os respectivos códigos se encontram nas pastas front (client) e back (server).


### Backend

Serviço: Hospedar o banco de dados e oferecer uma API para o frontend.

Linguagem: Javascript e Serverless Framework

Infraestrutura: AWS (S3 + Athena + Lambda functions + API Gateway)


### Frontend

Serviço: Consumir a API e disponibilizar uma interface de usuário.

Linguagem: Javascript

Infraestrutura: AWS (s3)


## Aplicativo WEB

A aplicação se encontra online em: http://bd-2020-1-trabalho-final.s3-website-us-east-1.amazonaws.com/

Mais instruções sobre como rodar localmente se encontram nas pasts back e front.
