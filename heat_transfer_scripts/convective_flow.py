import numpy as np
from pprint import pprint
import load
from load import unitMismatchError
"""
This file computes heat transfer using forced convection.

Authors:
    Steven ortega

Assumptions made:
    - Dittus-Boelter - Fully developed turbulent flow in a circular tube
    - Using a smooth channel
    - Circular channels

Notes:
    Before each calculation, specify the units needed for the equation.
    If the units for the property set in the yaml file don't match, an
    exception is raised to notify the user.
        psuedocode:         if yaml_diameter['units'] != 'mm:
                                raise unitMismatchError(...)
    
    If you convert units, then check that the unit comming in matches the
    conversion factor you specify.
        i.e.            YAML file says diameter in [mm]; Equation needs [m]
        psuedocode:
                        if yaml_diameter['units'] == 'mm':
                            diameter = {'val': yaml_diameter/1000, 'unit': 'm'}
                        else:
                            raise unitMismatchError(...)

"""

calcs = {}

#---------------------
# Setup the parameters
#---------------------
params = load.load_config('heat_transfer_scripts/setup.yaml')

try:
    load.checkUnits(params['cooling_jacket'])
    load.checkUnits(params['fluid_properties'])
except Exception as e:
    print(f'##########################\n')
    print(e)
    print(f'\n##########################')

jacket_p    = params['cooling_jacket']
fluid_p     = params['fluid_properties']


#----------------
# Reynolds Number
#----------------
# equation: Re = rho V D/ mu

rho = fluid_p['density']
V = fluid_p['velocity']
D = jacket_p['ID']
mu = fluid_p['viscosity']

if rho['unit'] != "Kg/m^3":
    raise unitMismatchError(f"density, {rho['unit']}")
if V['unit'] != "m/s":
    raise unitMismatchError(f"velocity, {V['unit']}")
if mu['unit'] != "Kg/m.s":
    raise unitMismatchError(f"viscosity, {mu['unit']}")
if D['unit'] == "mm":
    D = {'val' : D['val'] / 1000, 'unit': 'm'}
else:
    raise unitMismatchError(f"diameter, {D['unit']}")

calcs['Re'] = (rho['val'] * V['val'] * D['val'])/mu['val']

#-----------------------
# Get the Prandtl Number
#-----------------------
# eq: mu Cp / k

cp = fluid_p['cp']
k = fluid_p['k']
mu = fluid_p['viscosity']

if cp['unit'] != "J/Kg.K":
    raise unitMismatchError(f"cp, {cp['unit']}")
if k['unit'] != "W/m.K":
    raise unitMismatchError(f"k, {k['unit']}")
if mu['unit'] != "Kg/m.s":
    raise unitMismatchError(f"viscosity, {mu['unit']}")

calcs['Pr'] = (cp['val'] * mu['val'])/ k['val']

#-----------------------
# Get the Nusselt Number
#-----------------------
# Dittus–Boelter Eq
# eq: 0.023 Re^.8 Pr^.4

calcs['Nu'] = 0.023 * (calcs['Re']**.8) * (calcs['Pr']**.4)

#----------------------------------
# Get the Heat Transfer Coefficient
#----------------------------------
# For a smooth channel
# eq: Nu K / D
k = fluid_p['k']
D =  jacket_p['ID']

if k['unit'] != "W/m.K":
    raise unitMismatchError(f"k, {k['unit']}")
if D['unit'] == "mm":
    D = {'val' : D['val'] / 1000, 'unit': 'm'}
else:
    raise unitMismatchError(f"diameter, {D['unit']}")

calcs['h'] = (calcs['Nu'] * k['val']) / D['val']

#-----------------------------
# See everything we calculated 
print()
pprint(calcs)
print()
#-----------------------------