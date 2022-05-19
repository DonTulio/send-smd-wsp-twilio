import json
from os.path import join
from pathlib import Path
from json import load, dump
from typing import Dict


class Config:
    BASE_DIR = Path(__file__).parent.parent
    CONFIG_FILE = 'config.json'
    CONFIGURATION = {
        'ACCOUNT_SID': '',
        'AUTH_TOKEN': '',
        'DEFAULT_NUMBER': '',
        'SMS_SID': ''
    }

    def __init__(self) -> None:
        self.loadConfig()

    def loadConfig(self):
        try:
            with open(join(self.BASE_DIR, self.CONFIG_FILE)) as jsonConfig:
                print(jsonConfig)
                self.CONFIGURATION = load(jsonConfig)
        except FileNotFoundError as fne:
            print('Archivo de configuración no existe...')
            print('creando...')
            with open(join(self.BASE_DIR, self.CONFIG_FILE), 'w') as jsonConfig:
                dump({
                    'ACCOUNT_SID': '',
                    'AUTH_TOKEN': '',
                    'DEFAULT_NUMBER': '',
                    'SMS_SID': ''
                }, jsonConfig)
            exit(1)

    def getConfig(self) -> Dict:
        return self.CONFIGURATION
