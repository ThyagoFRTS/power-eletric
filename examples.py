from power_sizing import calculate_power_luminance
from power_sizing import calculate_number_and_power_of_tugs
from conductor_sizing import conduction_capacity
from conductor_sizing import minimum_section

#IMPORTANT: all inputs is in portuguese, remember this

# Calculate power luminance of an ambient
# inputs: Area (m^2)
calculate_power_luminance(12)

# Calculate power luminance of an ambient
# inputs: AmbientName (str), perimeter (m) 
calculate_number_and_power_of_tugs('sala',14)

# Sizing conductor by capacity conduction
# inputs: power (Watts/VA), Tension: optional (default 220), Potency-factor: optional (used if Watts, default 1)
conduction_capacity(3000, fp=0.8)

# Sizing conductor by section minimum
# inputs: Circuit type (str)
minimum_section('forca')