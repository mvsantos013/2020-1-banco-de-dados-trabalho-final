from src.utils import database as db

data = None

def handler(event, context):
  global data
  
  if(data is None or 'IS_LOCAL' in event):
    data = db.query(f'''SELECT * FROM `enderecos`;''')

  return {
    'statusCode': 200,
    'headers': { 'Access-Control-Allow-Origin': '*' },
    'body': data.to_json(orient='records')
  }