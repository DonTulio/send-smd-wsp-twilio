from core.Sms import Sms
from core.Whatsapp import Whatsapp
from utils.Config import Config
from os import system
class Menu:
    EXIT_OPTION = 3
    def __init__(self) -> None:
        self.option = 0
        Config().loadConfig()
        pass

    def showMenu(self):
        while self.option != self.EXIT_OPTION:
            system('cls')
            print('##'*5,'Elija una opción','#'*5)
            print('1) \t Para whatsapp')
            print('2) \t Para SMS')
            print('##'*5,'Elija una opción','#'*5)
            self.option = input('Escriba 1 o 2, 3 para salir: ')
            if self.option.isnumeric() == False:
                print('Debe ser una opción numérica...')
                input('Enter para continuar... ')
                continue
            self.option = int(self.option)
            if self.option == 1:
                number = input('Ingrese su número con el código de área y país: ')
                message = input('Ingrese el mensaje a enviar: ')
                Whatsapp().sendMessage(number=number,message=message)
            elif self.option == 2:
                number = input('Ingrese su número con el código de área y país: ')
                message = input('Ingrese el mensaje a enviar: ')
                Sms().sendMessage(number,message)
            elif self.option == 3:
                exit(0)
    