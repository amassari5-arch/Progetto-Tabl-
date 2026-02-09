from abc import ABC, abstractmethod
import os

class Menu(ABC):
    def __init__(self, nome_file):
        self.nome_file = nome_file
        self.piatti = {}
        self.percorso = os.path.join("..", "data", nome_file)

    @abstractmethod
    def carica_da_file(self):
        pass