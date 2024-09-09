from abc import ABC, abstractmethod

"""
El principio de inversión de dependencias establece que las clases de alto nivel 
no deben depender de las clases de bajo nivel. Ambos deben depender de abstracciones. 
Además, las abstracciones no deben depender de los detalles. 
Los detalles deben depender de las abstracciones.

Este ejemplo muestra cómo se puede aplicar el principio de inversión de dependencias. 
El ejemplo muestra cómo una clase FrontEnd depende de una clase BackEnd.
"""	
# #Bad example
# class FrontEnd:
#     def __init__(self, back_end):
#         self.__back_end = back_end

#     def display_data(self):
#         data = self.__back_end.get_data_from_database()
#         print("Display data:", data)


# class BackEnd:
#     def get_data_from_database(self):
#         """Return data from the database."""
#         return "Data from the database"


# Good example
class FrontEnd:
    def __init__(self, data_source):
        self.__data_source = data_source

    def display_data(self):
        data = self.__data_source.get_data()
        print("Display data:", data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass


class Database(DataSource):
    def get_data(self):
        return "Data from the database"


class API(DataSource):
    def get_data(self):
        return "Data from the API"
