from nbr_tables import get_conduction_table


def conduction_capacity(power, tension = 220, fp = 1, circuit_type = 'mono', installation_method = 'B1'):
  V = tension
  Ib = 0
  section = 0
  charged_conductors = '2'
  if circuit_type == 'mono':
    V = 220
    Ib = power/(V*fp)
  else:
    V = 380
    Ib = power/(V*1.71*fp)
    charged_conductors = '3'
  print('Project current: ', Ib)
  print('Monophase circuit')
  print('Charged conductors:', charged_conductors)

  methods, sections = get_conduction_table()

  for electric_current, index in zip(methods[installation_method][charged_conductors],methods[installation_method][charged_conductors].index):
    if float(electric_current.replace(',','.')) >= Ib:
      section = sections[index]
      print('Section: ', section)
      break

def minimum_section(circuit_type):
  if circuit_type == 'forca':
    return 2.5
  elif circuit_type == 'iluminacao':
    return 1.5
  elif circuit_type == 'controle':
    return 0.5
  else:
    print('no matches found')
    return 0