import configparser

class Config:
    def load(self, file):
        config = configparser.ConfigParser()
        config.read(file)
        return config


class DatabaseConfig(Config):
    def validate(self, config):
        return "host" in config["database"]


db = DatabaseConfig()
config = db.load("db.ini")

if "database" in config and db.validate(config):
    print("Config loaded successfully")
else:
    print("Invalid config")