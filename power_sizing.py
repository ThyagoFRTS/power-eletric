import math

def calculate_power_luminance(ambient_area):
  #area in m^2
  potency = 0
  if ambient_area <= 6:
    print('Lighting Potency: '+ str(100) +' (VA)')
    potency = 100
  else:
    print('extra potency: ' + str((ambient_area - 6)))
    potency = 100 +  60 * int((ambient_area - 6)/4)
    print('Lighting Potency: '+ str(potency) +' (VA)')
  print('')
  return potency
"""#Dimensionamento de TUGs"""

def calculate_number_and_power_of_tugs(ambient_name, perimeter = 0):
  #area in m^2
  #perimeter in m
  class1 = ['banheiro']
  class2 = ['cozinha', 'copa','copa-cozinha', 'area de servico', 'lavanderia']
  class3 = ['varanda']
  class4 = ['sala', 'quarto', 'dormitorio', 'escritorio']
  number_tugs = 0
  power_tugs = 0

  if ambient_name in class1:
    number_tugs = 1
    power_tugs = number_tugs * 600
  elif ambient_name in class2:
    number_tugs = math.ceil(perimeter/3.5)
    if number_tugs <= 3:
      power_tugs = number_tugs * 600
    else:
      power_tugs = 3 * 600 + 100 * (number_tugs - 3)
  elif ambient_name in class3:
    number_tugs = 1
    power_tugs = number_tugs * 100
  elif ambient_name in class4:
    number_tugs = math.ceil(perimeter/5)
    power_tugs = number_tugs * 100
  else:
    print('No matches found')
    print('warning: ambient is calculated by area, see in 54.10 norma\nEntry with area: ')
    area = float(input())
    if area <= 2.55:
      number_tugs = 1
      power_tugs = number_tugs * 100
    return 0
  print('Numbers TUG: ' + str(number_tugs) + '\nTUG Potency:' + str(power_tugs) +'(VA)')
  print('')
  return number_tugs, power_tugs
