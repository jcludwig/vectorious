# %%
from sympy import symbols
#from sympy.physics.mechanics import *
from sympy.physics import units

# %%
plywood_density = 760*units.kg/units.meter**3  # kg/m^3

beam_length = 1*units.meter
beam_width = units.convert_to(2*units.centimeter, units.meter)
beam_thickness = units.convert_to(.75*units.inch, units.meter)

beam_volume = beam_length*beam_width*beam_thickness
beam_weight = plywood_density*beam_volume

print(beam_weight)