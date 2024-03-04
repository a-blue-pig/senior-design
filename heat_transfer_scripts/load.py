import yaml
import pprint

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
        except yaml.YAMLError as exc:
            print(exc)

if __name__ == "__main__":
    parameters = load_config("heat_transfer_scripts/setup.yaml")
    pprint.pprint(parameters)


    