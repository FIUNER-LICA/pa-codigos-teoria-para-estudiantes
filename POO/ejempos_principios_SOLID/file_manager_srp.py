from pathlib import Path
from zipfile import ZipFile

""" 
El principio de responsabilidad única establece que una clase debe tener una sola razón
para cambiar.

Este ejemplo muestra como se puede aplicar el principio de responsabilidad única.
"""	
# Bad example
# class FileManager:
#     def __init__(self, filename):
#         self.__path = Path(filename)

#     def read(self, encoding="utf-8"):
#         return self.__path.read_text(encoding)

#     def write(self, data, encoding="utf-8"):
#         self.__path.write_text(data, encoding)

#     def compress(self):
#         with ZipFile(self.__path.with_suffix(".zip"), mode="w") as archive:
#             archive.write(self.__path)

#     def decompress(self):
#         with ZipFile(self.__path.with_suffix(".zip"), mode="r") as archive:
#             archive.extractall()


# Good example
class FileManager:
    def __init__(self, filename):
        self.__path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.__path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.__path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
