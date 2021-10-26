from power_sizing import calculate_power_luminance
from power_sizing import calculate_number_and_power_of_tugs
from conductor_sizing import conduction_capacity
from conductor_sizing import minimum_section
from conductor_sizing import voltage_drop
from conductor_sizing import harmonic_rate
from neutral_sizing import get_neutral_section
from protection_sizing import get_conductor_protection_section
import pathlib
#IMPORTANT: all inputs is in portuguese, remember this

# Calculate power luminance of an ambient
# inputs: Area (m^2)
calculate_power_luminance(12)

# Calculate power luminance of an ambient
# inputs: AmbientName (str), perimeter (m) 
calculate_number_and_power_of_tugs('sala',14)

# Sizing conductor by capacity conduction
# inputs: power (Watts/VA), tension: optional (default 220), Potency-factor: optional (used if Watts, default 1)
# circuit_type: optional mono/tri (str) (default mono)    
section1 = conduction_capacity(21000, fp=0.9 ,ft=0.87, fg=0.8, circuit_type='tri')

# Sizing conductor by section minimum
# inputs: Circuit type (str)
section2 =  minimum_section('forca')

# Sizing conductor by voltage drop
# inputs: power (Watts/VA), distance in (m), fp: (default 1), circuit_type: optional 'mono'/'tri' (default 'mono')
# isolation_type = optional 0 to Non-Magnetic 1 to Magnetic (default 0), drop_rate: optional (default 0.04)
section3 = voltage_drop(13000,40, drop_rate=0.02, circuit_type='tri', fp = 0.75, isolation_type = 0)

# Sizing conductor by harmonic
# inputs: harmonics [I1, I3, I5...] circuit_type: optional 'tri'/'bi' (default 'tri')
section4, thd3 = harmonic_rate(harmonics = [100,60,45,30,20], fp = 1, ft=1, fg=1 , circuit_type = 'tri', installation_method = 'B1')

# Sizing neutral
# inputs: phase_section (mm), Ib: project current, balanced_circuit: optional bool (default True), circuit_type: optional 'mono'/'tri'  (default 'mono')
get_neutral_section(95, 10, circuit_type = 'tri', index_THD3 = 0.14, balanced_circuit = True)


# Sizing protection
# inputs: phase_section (mm)
get_neutral_section(70, 130, circuit_type = 'tri', index_THD3 = 0.6, balanced_circuit = True, installation_method = 'B1', ft=1, fg=1)