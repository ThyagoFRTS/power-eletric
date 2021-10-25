#WARNNING: this method dont changes all European data
#change each value with lambda function if necessary
import pandas as pd
import pathlib

script_dir = pathlib.Path(__file__).parent.resolve()


def get_conduction_table():
  table_conduction = pd.read_csv(str(script_dir)+'/tables/coduction_capacity_cu.csv', decimal=',')
  methods = table_conduction[table_conduction.columns[1:]]
  sections = table_conduction.Section.drop([0])

  data = {}
  unnamed_columns = []
  installation_methods = []
  for column in methods.columns: unnamed_columns.append(column) if 'Unnamed' in column else installation_methods.append(column)
  
  for method, unnamed_column in zip(installation_methods, unnamed_columns):
    method_2_3_conductors = pd.concat([table_conduction[method], table_conduction[unnamed_column]],axis= 1)
    method_2_3_conductors = method_2_3_conductors.drop([0,0])
    method_2_3_conductors.columns = ['2','3']
    data[method] = method_2_3_conductors
  return data,sections
