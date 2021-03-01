from src.utils import database as db

data = None

query_string = """ 
SELECT
CASE
WHEN T.Ano_Nascimento between 1930 and 1940 then 'Entre 80 e 90 anos'
WHEN T.Ano_Nascimento between 1941 and 1950 then 'Entre 70 e 80 anos'
WHEN T.Ano_Nascimento between 1951 and 1960 then 'Entre 60 e 70 anos'
WHEN T.Ano_Nascimento between 1961 and 1990 then 'Entre 30 e 60 anos'
WHEN T.Ano_Nascimento between 1991 and 2021 then 'Entre 0 e 30 anos'
END as faixas, SUM(T.Proporcao_Obito) as Proporcao_Obito FROM
   (SELECT
       PAC.aa_nascimento as Ano_Nascimento,
       COALESCE(T1.SOMA_ALTA / COUNT(*), 0) as Proporcao_Alta_Medica,
       COALESCE(T2.OBITO / COUNT(*), 0) as Proporcao_Obito,
       COALESCE(T3.SOMA_ADM / COUNT(*), 0) as Proporcao_Alta_Administrativa
   FROM
    pacientes as PAC
   INNER JOIN
     atendimentos AS ATD on ATD.id_paciente = PAC.id
   INNER JOIN
    desfechos AS DES on ATD.id = DES.id_atendimento
   INNER JOIN
     tipos_de_desfecho AS TIP on TIP.id = DES.id_tipo_desfecho
   LEFT JOIN
    (SELECT COUNT(*) AS SOMA_ADM, PAC.aa_nascimento as ANO FROM pacientes AS PAC inner join atendimentos as ATD on ATD.id_paciente = PAC.id INNER JOIN
        desfechos AS DES on DES.id_atendimento = ATD.id INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho like '%Alta administrativa%' GROUP BY PAC.aa_nascimento) as T3 on T3.ANO = PAC.aa_nascimento
   LEFT JOIN
    (SELECT COUNT(*) AS SOMA_ALTA, PAC.aa_nascimento as ANO FROM pacientes AS PAC inner join atendimentos as ATD on ATD.id_paciente = PAC.id INNER JOIN
        desfechos AS DES on DES.id_atendimento = ATD.id INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho in ('Alta médica melhorado', 'Alta médica curado') GROUP BY PAC.aa_nascimento) as T1 on T1.ANO = PAC.aa_nascimento
   LEFT JOIN
     (SELECT COUNT(*) AS OBITO, PAC.aa_nascimento as ANO FROM pacientes AS PAC inner join atendimentos as ATD on ATD.id_paciente = PAC.id INNER JOIN
        desfechos AS DES on DES.id_atendimento = ATD.id INNER JOIN tipos_de_desfecho AS TIP ON TIP.id = DES.id_tipo_desfecho WHERE TIP.desfecho like '%Óbito%' GROUP BY PAC.aa_nascimento) as T2 on T2.ANO = PAC.aa_nascimento
   GROUP BY
     PAC.aa_nascimento) as T
GROUP BY faixas
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