import yaml

def load_config(file_path: str):
    """
    Load a YAML configuration file.
    :param file_path: Path to the YAML file.
    :return: Parsed configuration as a dictionary.
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)