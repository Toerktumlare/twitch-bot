from abc import ABC, abstractmethod

class BaseCommand(ABC):
    def __init__(self, command):
        super().__init__()
        self.command = command

    @abstractmethod
    def is_match(self):
        if(command == self.command):
            return True
        return False

    @abstractmethod
    def process(self, command):
        pass