import random

from commands.base_command import BaseCommand 

class Dice(BaseCommand):
    def __init__(self, command, commandType, channel):
        super().__init__(command, commandType, channel)

    def is_match(self, response):
        str_array = response.split(":")
        if(len(str_array) == 3 and str_array[2].rstrip() == self.command):
            return True
        return False

    def execute(self, response):
        print(f'\U0001F3BE Returning random number to chat')
        return self.commandType + " #" + self.channel + " :" + str(random.randrange(1, 7))