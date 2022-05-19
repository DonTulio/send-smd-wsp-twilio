from twilio.rest import Client
from utils.Config import Config
# Cargamos la configuración
class Whatsapp:
    def __init__(self) -> None:
        self.config = Config()
        print(self.config.BASE_DIR)
        print(self.config.CONFIGURATION)
        self.client = Client(self.config.CONFIGURATION['ACCOUNT_SID'], self.config.CONFIGURATION['AUTH_TOKEN'])
    def sendMessage(self, number: str, message: str) -> None:
        number = f'whatsapp:{number}'
        try:
            self.client.messages.create(
                body = message,
                from_= self.config.CONFIGURATION['DEFAULT_NUMBER'],
                to=number
            )
        except Exception as e:
            print('Ocurrio un error...')
            print(e)
    

