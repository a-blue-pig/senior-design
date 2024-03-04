import yaml
from pprint import pprint
import re

# List of units that are valid 
metric_units = [
    'mm', 'm', 'cm',    # Length
    'L',                # Volume
    'Kg', 'g',          # Mass
    'N',                # Force
    's',                # Time
    'W',                # Power
    'K', 'C',           # Temperature
    'Pa',               # Pressure
    'J',                # Energy
    'placeholder',      # Skip errors during dev
    'na'                # No units
]

class InvalidUnitsError(Exception):
    """Exception thrown when invalid units are detected."""
    def __init__(self, bad_units):
        self.bad_units = bad_units
        super().__init__(f"Invalid units detected:\n{bad_units}")

class unitMismatchError(Exception):
    """Let the user know that there is a unit mismatch."""
    def __init__(self, units):
        self.units = units
        msg = f"\n---------------------------------------"  \
              f"\nUnit mismatch. Is this correct?\n{units}\n" \
              f"---------------------------------------\n"
        super().__init__(msg)

def checkUnits(param_list: dict):
    """Checks the units of the provided param_list against allowed units 
    in the metric_units array.

    Args:
        param_list (dict): A dictionary with all the parameter names, values,
                           and units for the parameter.

    Raises:
        InvalidUnitsError: Raised if the units are not in metric_units
    """
    invalid_units = []
    for k, v in param_list.items():
        units = re.findall(r'[a-zA-Z]+', v['unit'])
        if not all(unit in metric_units for unit in units):
            invalid_units.append(k)
            print(f'\n---------------------------------------')
            print(f'Is {v['unit']} a metric unit?')
            print(f'---------------------------------------\n')

    if invalid_units:
        incorrect_units = ""
        for p in invalid_units:
            incorrect_units += f"{p}, {param_list[p]['unit']}"
        raise InvalidUnitsError(incorrect_units)

def load_config(file_path: str = "config.yaml") -> dict:
    """Reads the provided yaml file in file_path and extracts the parameters.

    Args:
        file_path (str): The filepath to the .yaml file with the parameters
                         to load into a dictionary

    Returns:
        dict: A dictionary mapping of the yaml file parameters
    """
    with open(file_path) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)

if __name__ == "__main__":
    parameters = load_config("heat_transfer_scripts/setup.yaml")
    pprint(parameters)


    