from power_sizing import calculate_power_luminance
from power_sizing import calculate_number_and_power_of_tugs
from conductor_sizing import conduction_capacity
from conductor_sizing import minimum_section
from conductor_sizing import voltage_drop
import pathlib
#IMPORTANT: all inputs is in portuguese, remember this

# Calculate power luminance of an ambient
# inputs: Area (m^2)
calculate_power_luminance(12)

# Calculate power luminance of an ambient
# inputs: AmbientName (str), perimeter (m) 
calculate_number_and_power_of_tugs('sala',14)

# Sizing conductor by capacity conduction
# inputs: power (Watts/VA), Tension: optional (default 220), Potency-factor: optional (used if Watts, default 1)
# Circuit Type: optional mono/tri (str) (default mono)    
conduction_capacity(21000, fp=0.9 ,ft=0.87, fg=0.8, circuit_type='tri')

# Sizing conductor by section minimum
# inputs: Circuit type (str)
minimum_section('forca')

# Sizing conductor by voltage drop
# inputs: power (Watts/VA), distance in (m)
# See a value less than your voltage drop on voltage drop table on internet (not disponible in this repository)
voltage_drop(5400,15)