# Backend

Esta é uma aplicação feita com a Serverless Framework.

# How to invoke an API endpoint locally

```bash
# make sure you have serverless installed
npm install -g serverless

serverless invoke local -f pacientes # pacientes endpoint
serverless invoke local -f desfechos # desfechos endpoint
serverless invoke local -f exames # exames endpoint
```

nota: Solicite as credenciais AWS (credentials.yml) para executar a API localmente.


## API endpoints

Base PATH

https://ohup21d337.execute-api.us-east-1.amazonaws.com/dev/api

Endpoints

- /pacientes
- /desfechos
- /exames

