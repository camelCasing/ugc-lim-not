import os

# Future config module

class Config:
    def __init__(self, location) -> None:
        self.location = location
        self.configFile = None
        self.configText = ""

        if os.path.exists(location):
            self.configFile = open(location, "r")
            self.configText = self.configFile.read()
            self.configFile.close()
        else:
            Exception("FConfig: Config file does not exist")

    def get(self, configProperty: str):
        for line in self.configText.splitlines():
            if line.startswith(configProperty):
                configValue = line.split("=")[1]

                return configValue
            
        return None
