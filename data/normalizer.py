import pandas as pd

def normaliza_pacientes():
  pacientes = pd.read_csv('./HSL_Pacientes_2.csv', delimiter="|")

  paises = pacientes['CD_PAIS']
  paises = list(set(paises))
  paises = [x for x in paises if x == x]
  paises_df = pd.DataFrame(paises, columns=["CD_PAIS"])
  paises_df.index.name = "ID_PAIS"

  estados = pacientes['CD_UF']
  estados = list(set(estados))
  estados = [x for x in estados if x == x]
  estados_df = pd.DataFrame(estados, columns=["CD_UF"])
  estados_df.index.name = "ID_UF"

  municipios = pacientes['CD_MUNICIPIO']
  municipios = list(set(municipios))
  municipios = [x for x in municipios if x == x]   
  municipios_df = pd.DataFrame(municipios, columns=["CD_MUNICIPIO"])
  municipios_df.index.name = "ID_MUNICIPIO"

  sexos = pacientes['IC_SEXO']
  sexos = list(set(sexos))
  sexos = [x for x in sexos if x == x]   
  sexos_df = pd.DataFrame(sexos, columns=["IC_SEXO"])
  sexos_df.index.name = "ID_SEXO"

  def relaciona(row):
    id_pais = paises_df.index[paises_df['CD_PAIS'] == row['CD_PAIS']].tolist()
    row['CD_PAIS'] = str(id_pais[0]) if len(id_pais) > 0 else None

    id_estado = estados_df.index[estados_df['CD_UF'] == row['CD_UF']].tolist()
    row['CD_UF'] = str(id_estado[0]) if len(id_estado) > 0 else None

    id_municipio = municipios_df.index[municipios_df['CD_MUNICIPIO'] == row['CD_MUNICIPIO']].tolist()
    row['CD_MUNICIPIO'] = str(id_municipio[0]) if len(id_municipio) > 0 else None

    id_sexo = sexos_df.index[sexos_df['IC_SEXO'] == row['IC_SEXO']].tolist()
    row['ID_SEXO'] = str(id_sexo[0]) if len(id_sexo) > 0 else None

    return row

  pacientes = pacientes.apply(relaciona, axis=1)
  pacientes.rename(columns = {'CD_PAIS': 'ID_PAIS', 'CD_UF': 'ID_UF', 'CD_MUNICIPIO': 'ID_MUNICIPIO'}, inplace = True) 

  enderecos = pacientes.copy()[['ID_PAIS', 'ID_UF', 'ID_MUNICIPIO', 'CD_CEPREDUZIDO']]
  enderecos.index.name = "ID_ENDERECO"

  pacientes = pacientes[['ID_PACIENTE', 'ID_SEXO', 'AA_NASCIMENTO']]
  pacientes['ID_ENDERECO'] = enderecos.index.tolist()

  pacientes.to_csv('./data/pacientes.csv', index=False)
  paises_df.to_csv('./data/paises.csv')
  estados_df.to_csv('./data/estados.csv')
  municipios_df.to_csv('./data/municipios.csv')
  enderecos.to_csv('./data/enderecos.csv')
  sexos_df.to_csv('./data/sexos.csv')


def normaliza_desfechos():
  desfechos = pd.read_csv('./HSL_Desfechos_2.csv', delimiter="|")

  atendimentos = desfechos.copy()[['id_atendimento', 'dt_atendimento', 'de_tipo_atendimento']]

  tipos_de_atendimento = atendimentos['de_tipo_atendimento']
  tipos_de_atendimento = list(set(tipos_de_atendimento))
  tipos_de_atendimento = [x for x in tipos_de_atendimento if x == x]   
  tipos_de_atendimento_df = pd.DataFrame(tipos_de_atendimento, columns=["nome"])
  tipos_de_atendimento_df.index.name = "id_tipo_atendimento"

  def relaciona(row):
    id_tipo_atendimento = tipos_de_atendimento_df.index[tipos_de_atendimento_df['nome'] == row['de_tipo_atendimento']].tolist()
    row['de_tipo_atendimento'] = str(id_tipo_atendimento[0]) if len(id_tipo_atendimento) > 0 else None
    return row

  atendimentos = atendimentos.apply(relaciona, axis=1)
  atendimentos.rename(columns = {'de_tipo_atendimento': 'id_tipo_atendimento'}, inplace = True) 

  clinicas = desfechos.copy()[['id_clinica', 'de_clinica']]
  clinicas = clinicas.drop_duplicates(subset=['id_clinica'])

  desfechos = desfechos[['id_paciente', 'id_atendimento', 'id_clinica', 'dt_desfecho', 'de_desfecho']]

  tipos_de_desfecho = desfechos['de_desfecho']
  tipos_de_desfecho = list(set(tipos_de_desfecho))
  tipos_de_desfecho = [x for x in tipos_de_desfecho if x == x]   
  tipos_de_desfecho_df = pd.DataFrame(tipos_de_desfecho, columns=["nome"])
  tipos_de_desfecho_df.index.name = "id_tipo_desfecho"

  def relaciona(row):
    id_tipo_desfecho = tipos_de_desfecho_df.index[tipos_de_desfecho_df['nome'] == row['de_desfecho']].tolist()
    row['de_desfecho'] = str(id_tipo_desfecho[0]) if len(id_tipo_desfecho) > 0 else None
    return row

  desfechos = desfechos.apply(relaciona, axis=1)
  desfechos.rename(columns = {'de_desfecho': 'id_tipo_desfecho'}, inplace = True) 

  desfechos.to_csv('./data/desfechos.csv', index=False)
  atendimentos.to_csv('./data/atendimentos.csv', index=False)
  clinicas.to_csv('./data/clinicas.csv', index=False)
  tipos_de_atendimento_df.to_csv('./data/tipos_de_atendimento.csv')
  tipos_de_desfecho_df.to_csv('./data/tipos_de_desfecho.csv')


def normaliza_exames():
  exames = pd.read_csv('./HSL_Exames_2.csv', delimiter="|")

  locais_de_exame = exames['DE_ORIGEM']
  locais_de_exame = list(set(locais_de_exame))
  locais_de_exame = [x for x in locais_de_exame if x == x]
  locais_de_exame_df = pd.DataFrame(locais_de_exame, columns=["NOME"])
  locais_de_exame_df.index.name = "ID_LOCAL_EXAME"

  tipos_de_exame = exames['DE_EXAME']
  tipos_de_exame = list(set(tipos_de_exame))
  tipos_de_exame = [x for x in tipos_de_exame if x == x]
  tipos_de_exame_df = pd.DataFrame(tipos_de_exame, columns=["NOME"])
  tipos_de_exame_df.index.name = "ID_TIPO_EXAME"

  def relaciona(row):
    id_exame = locais_de_exame_df.index[locais_de_exame_df['NOME'] == row['DE_ORIGEM']].tolist()
    row['DE_ORIGEM'] = str(id_exame[0]) if len(id_exame) > 0 else None

    id_tipo_de_exame = tipos_de_exame_df.index[tipos_de_exame_df['NOME'] == row['DE_EXAME']].tolist()
    row['DE_EXAME'] = str(id_tipo_de_exame[0]) if len(id_tipo_de_exame) > 0 else None

    return row

  exames = exames.apply(relaciona, axis=1)
  exames.rename(columns = {'DE_ORIGEM': 'ID_LOCAL_EXAME', 'DE_EXAME': 'ID_TIPO_EXAME'}, inplace = True) 

  exames.to_csv('./data/exames.csv', index=False)
  locais_de_exame_df.to_csv('./data/locais_de_exame.csv')
  tipos_de_exame_df.to_csv('./data/tipos_de_exame.csv')

#normaliza_pacientes()
#normaliza_desfechos()
#normaliza_exames()
