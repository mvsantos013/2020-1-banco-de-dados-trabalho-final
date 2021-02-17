import os
import pandas as pd
import mysql.connector as mysql

DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

connection = None

def get_connection():
  global connection 

  if(connection is not None):
    return connection

  connection = mysql.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
  return connection

def query(sql_string):
  return pd.read_sql(sql_string, con=get_connection())