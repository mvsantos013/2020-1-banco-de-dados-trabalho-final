from src.utils import database as db

data = None

query_string = """ 
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
  (SELECT COUNT(*) AS SOMA_ADM, DES.dt_desfecho FROM desfechos AS DES INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho like '%Administrativa%' GROUP BY DES.dt_desfecho) as T on T.dt_desfecho = DES.dt_desfecho
GROUP BY
  DES.dt_desfecho
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