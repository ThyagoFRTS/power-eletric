# Power Eletric
<p align='center' >Power Eletric is a module python to resolve and sizing eletrical installations problems, based on NBR 5410:2004</p>

## Project Status

<p>Under development</p>

## Features

- Power sizing (TUG & lighting)
- Conductors sizing by Minimum Section
- Conductors sizing by Coduction Capacity
- Conductors sizing by Voltage Drop
- Conductors sizing by Harmonic Rate
- Neutral sizing
- Protection Conductor sizing

## How to Use
<p>All input parametters is in portuguese</p>

### Examples

#### Calculate Luminance
```
area = 12
potency = calculate_power_luminance(area)
```
#### Calculate TUG power
```
area = 12
number_tugs, power_tugs = calculate_power_luminance(area)
```

#### Calculate Phase section by Conduction Capacity
```
potency = 15000
phase_section1 = conduction_capacity(potency, fp=0.9 ,ft=0.87, fg=0.8, circuit_type='mono')
```

#### Calculate Neutral section
```
phase_section = 95
Ib = 10
neutral_section1 = get_neutral_section(phase_section, Ib, circuit_type = 'tri', index_THD3 = 0.14, balanced_circuit = True)
```

#### Calculate Protection section
```
phase_section = 95
protection_section1 = get_conductor_protection_section(phase_section)
```

<p>See examples.py to get other methods </p>

## How to Install

<p>By now, this project is no exportable to python packages </p>
<p>Git clone or download zip files</p>

### Dependencies

- Pandas v1.1.5 or higher

## Technologies

- Python 3.10

## Author

- Thyago Rodrigues (ThyagoKZKR)

## License & copyright

© Thyago M. Rodrigues

Licensed under [MIT License](LICENSE)

