from abc import ABC, abstractmethod

class BaseCommand(ABC):
    def __init__(self, command):
        super().__init__()
        self.command = command

    @abstractmethod
    def is_match(self, response):
      return False  
            
        

    @abstractmethod
    def execute(self, command):
      return None