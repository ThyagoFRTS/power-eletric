from nbr_tables import get_conduction_table


def conduction_capacity(power, tension = 220, fp = 1, ft=1, fg=1 , circuit_type = 'mono', installation_method = 'B1'):
  V = tension
  Ib = 0
  section = 0
  charged_conductors = '2'
  if circuit_type == 'mono':
    circ_type = 'Monophase circuit'
    Ib = power/(V*fp)
    Ib1 = power/(V*fp*ft*fg)
  elif circuit_type == 'tri':
    circ_type = 'Triphase circuit'
    V = 380
    Ib = power/(V*1.732*fp)
    Ib1 = power/(V*1.732*fp*ft*fg)
    charged_conductors = '3'
  else:
    print('No maches found')
    return -1
  print('Project current: ', Ib)
  print('Current to table: ', Ib1)
  print(circ_type)
  print('Charged conductors:', charged_conductors)

  methods, sections = get_conduction_table()

  capacity_cable = 1

  for electric_current, index in zip(methods[installation_method][charged_conductors],methods[installation_method][charged_conductors].index):
    i = float(str(electric_current).replace(',','.'))
    if i >= Ib1:
        section = sections[index]
        capacity_cable = i
        if (i*fp*fg < Ib):
          print("Normal conditions, cable with sectinon "+str(section)+" supports "+str(i)+', but with ft and fg, the real capacity is:'+ str(i*ft*fg))
          continue
        print('Section by Conduction Capacity: ', section)
        break

  if fg != 1 or ft !=1:
    print("Normal conditions, cable supports "+str(i)+', but with ft and fg, the real capacity is:'+ str(i*ft*fg))
  
  



def minimum_section(circuit_type):
  if circuit_type == 'forca':
    print('Section by Minimum Section: ', 2.5)
    return 2.5
  elif circuit_type == 'iluminacao':
    print('Section by Minimum Section: ', 1.5)
    return 1.5
  elif circuit_type == 'controle':
    print('Section by Minimum Section: ', 0.5)
    return 0.5
  else:
    print('no matches found')
    return 0

def voltage_drop(power, size_conductor, drop_rate = 0.04, tension = 220, fp = 1, circuit_type = 'mono', installation_method = 'B1'):
  Ib = 0
  V = tension
  size_conductor = size_conductor/1000
  if circuit_type == 'mono':
    circ_type = 'Monophase circuit'
    Ib = power/(V*fp)
  elif circuit_type == 'tri':
    circ_type = 'Triphase circuit'
    V = 380
    Ib = power/(V*1.732*fp)
    charged_conductors = '3'
  else:
    print('No maches found')
    return -1
  
  voltage_rate = (drop_rate * tension)/(Ib * size_conductor)
  print('Voltage drop: '+str(voltage_rate))
  return voltage_rate