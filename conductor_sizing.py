#from powereletric.nbr_tables import get_conduction_table
from nbr_tables import get_conduction_table
from nbr_tables import get_tension_drop_table
import math

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
  print('')
  



def minimum_section(circuit_type):
  section = 0
  if circuit_type == 'forca':
    print('Section by Minimum Section: ', 2.5)
    section =  2.5
  elif circuit_type == 'iluminacao':
    print('Section by Minimum Section: ', 1.5)
    section =  1.5
  elif circuit_type == 'controle':
    print('Section by Minimum Section: ', 0.5)
    section =  0.5
  else:
    print('no matches found')
    return -1
  print('')
  return section




def voltage_drop(power, size_conductor, drop_rate = 0.04, tension = 220, fp = 1, isolation_type = 0, circuit_type = 'mono', installation_method = 'B1'):
  Ib = 0
  V = tension
  size_conductor = size_conductor/1000
  circuit = 'Mono'
  isolations = ['Non-Magnetic', 'Magnetic']
  
  if circuit_type == 'mono':
    Ib = power/(V*fp)
  elif circuit_type == 'tri':
    circuit = 'Tri'
    V = 380
    Ib = power/(V*1.732*fp)
    charged_conductors = '3'
  else:
    print('No maches found')
    return -1
  
  
  voltage_rate = (drop_rate * V)/(Ib * size_conductor)
  data, sections = get_tension_drop_table()
  fp_selected = '0.8' if abs(fp - 0.8) < abs(fp - 0.95)  else '0.95'

  print('Project current: ', Ib)
  print('Conductor size (km)',size_conductor)
  print('Tension: ',V)
  print('Voltage drop: '+str(voltage_rate))
  print('Power factor selectd to enter on table: ',fp_selected)
  
  table = data[isolations[isolation_type]]
  if isolation_type == 1:
    for electric_current, index in zip(table['MonoTri'][fp_selected], table['MonoTri'][fp_selected].index):
      if float(electric_current) <= voltage_rate:
        section = sections[index]
        print('Section: ', section)
        break
  else:
    for electric_current, index in zip(table[circuit][fp_selected], table[circuit][fp_selected].index):  
      if float(electric_current) <= voltage_rate:
        section = sections[index]
        print('Section: ', section)
        break
  print('')
  return voltage_rate, section

def harmonic_rate(harmonics = [], fp = 1, ft=1, fg=1 , circuit_type = 'mono', installation_method = 'B1'):
  Ib = math.sqrt(sum([harmonic**2 for harmonic in harmonics]))
  if len(harmonics)>=2:
    THD3 = 100 * harmonics[1]/harmonics[0]
    print('Project current: ', Ib)
    print('THD3 (%): ', THD3)
    if THD3 > 33:
      Ib = Ib/0.86

      print('Adjusting Project current: ', Ib)
  
  if circuit_type == 'mono':
    charged_conductors = '2'
  elif circuit_type == 'tri':
    charged_conductors = '3'
  else:
    print('No maches found')
    return -1
  
  Ib1 = Ib
  if fg != 1 or ft !=1:
    print('entro')
    Ib1 = Ib/(fg*ft)
    
  print('Current to table: ', Ib1)
  
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
  print('')
  