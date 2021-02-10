import os
import pandas as pd
from pyathena import connect

connection = None

def get_connection():
  global connection 

  if(connection is not None):
    return connection

  connection = connect(
    aws_access_key_id=os.environ['DB_KEY'], 
    aws_secret_access_key=os.environ['DB_SECRET'], 
    s3_staging_dir='s3://bd-2020-1-trabalho-final/data/stg/', 
    region_name='us-east-1'
  )

  return connection

def query(sql_string, connection):
  return pd.read_sql(sql_string, connection)