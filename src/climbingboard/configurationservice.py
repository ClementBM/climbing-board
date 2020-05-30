import yaml


class ConfigurationService(object):
    def get_setting(self, setting_key: str):
        with open("config.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg[setting_key]

