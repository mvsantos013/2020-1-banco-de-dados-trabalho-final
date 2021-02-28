from src.utils import database as db

data = None

query_string = """ 
SELECT 
  tipos_de_desfecho.desfecho as Desfecho,
  COUNT(*) as Quantidade 
FROM 
  atendimentos
INNER JOIN 
  desfechos on atendimentos.id = desfechos.id_atendimento
INNER JOIN
  tipos_de_desfecho on tipos_de_desfecho.id = desfechos.id_tipo_desfecho
GROUP BY
  tipos_de_desfecho.desfecho
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