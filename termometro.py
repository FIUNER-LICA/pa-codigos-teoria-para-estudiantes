import random

class Sensor:
    def sensar(self):
        return random.randint(0, 500)/100
    
class Conversor:
    def convertir(self, p_valor):
        return -20 + (120 -(-20))/(5-0)*p_valor
    
class Termometro:
    def __init__(self):
        self.__sensor = Sensor()
        self.__conversor = Conversor()

    def medirTemperatura(self):
        voltaje = self.__sensor.sensar()
        temperatura = self.__conversor.convertir(voltaje)
        return temperatura
    

if __name__ == "__main__":
    termometro = Termometro()

    for _ in range(5):
        print(round(termometro.medirTemperatura(), 2))