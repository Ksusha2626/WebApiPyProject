import yaml


class HostConfig(object):
    """Parser for host config"""

    def __init__(self, path_to_yaml=None):
        self.host_config = self.parse_yaml(path_to_yaml) if path_to_yaml else {}

    @staticmethod
    def parse_yaml(file_yaml):
        """Parse any yaml and return it as dict."""
        with open(file_yaml) as f:
            parsed_yaml = yaml.safe_load(f)
        return parsed_yaml
