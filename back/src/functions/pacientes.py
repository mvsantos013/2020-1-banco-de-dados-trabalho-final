from src.utils import database as db

data = None

def handler(event, context):
  global data
  
  connection = db.get_connection()

  if(data is None):
    data = db.query(''' SELECT * FROM "bd_2020_1"."pacientes" ''', connection)

  return {
    'statusCode': 200,
    'headers': { 'Access-Control-Allow-Origin': '*' },
    'body': data.to_json(orient='records')
  }