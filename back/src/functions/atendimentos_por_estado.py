from src.utils import database as db

data = None

query_string = """ 
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
"""

def handler(event, context):
  global data
  
  if(data is None or 'IS_LOCAL' in event):
    data = db.query(query_string)

  return {
    'statusCode': 200,
    'headers': { 'Access-Control-Allow-Origin': '*' },
    'body': data.to_json(orient='records')
  }