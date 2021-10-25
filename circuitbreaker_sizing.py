def conduction_capity(power, tension = 220, fp = 1, ft=1, fg=1 , circuit_type = 'mono', installation_method = 'B1'):
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