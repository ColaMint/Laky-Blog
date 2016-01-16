import yaml

setting = {}

def parse_config_file(filepath):
    with open(filepath) as stream:
        setting.update(yaml.load(stream))
