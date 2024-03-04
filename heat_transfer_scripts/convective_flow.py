import numpy as np
import load
"""
This file computes heat transfer using forced convection.

Authors:
    Steven ortega


Assumptions made:


"""

# this file works in metric values
metric_units = [
    'mm', 'm',      # Length
    'm^2'           # Area
    'm^3', 'L'      # Volume
    'Kg',           # Mass
    'N',            # Force
    's',            # Time
    'W',            # Power
    'K', 'C',       # Temperature
    'Pa',           # Pressure
    'J'             # Energy
]

params = load.load_config('heat_transfer_scripts/setup.yaml')