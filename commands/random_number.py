import random

from commands.base_command import BaseCommand 

class RandomNumber(BaseCommand):
    def __init__(self, command, commandType):
        super().__init__(command, commandType)

    def is_match(self, response):
        str_array = response.split(":")
        if(str_array[2].rstrip() == self.command):
            return True
        return False

    def execute(self, response):
        print(f'\U0001F3BE Returning random number to chat')
        return self.commandType + " #toerktumlare :" + str(random.randrange(1, 11))