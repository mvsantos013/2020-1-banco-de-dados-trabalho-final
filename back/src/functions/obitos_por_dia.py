from src.utils import database as db

data = None

query_string = """ 
SELECT dt_desfecho, COUNT(DISTINCT id_atendimento) AS obitos FROM desfechos
WHERE id_tipo_desfecho IN (SELECT id FROM tipos_de_desfecho WHERE desfecho LIKE '%Óbito%')
GROUP BY dt_desfecho
order by dt_desfecho ASC
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