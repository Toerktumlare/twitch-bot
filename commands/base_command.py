from abc import ABC, abstractmethod

class BaseCommand(ABC):
    def __init__(self, command, commandType):
        super().__init__()
        self.command = command
        self.commandType = commandType

    @abstractmethod
    def is_match(self, response):
      return False  
            
    @abstractmethod
    def execute(self, command):
      return None