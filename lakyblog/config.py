import yaml

config = {}

def parse_config_file(filepath):
    with open(filepath) as stream:
        config.update(yaml.load(stream))
