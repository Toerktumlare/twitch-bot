import random
import os

from commands.base_command import BaseCommand 

class Compliment(BaseCommand):
    def __init__(self, command, commandType):
        super().__init__(command, commandType)
        filePath = os.path.join(os.path.dirname(__file__), 'compliments.txt')
        self.compliments = open(filePath, "r").read().splitlines()

    def is_match(self, response):
        str_array = response.split(":")
        if(str_array[2].rstrip() == self.command):
            return True
        return False

    def execute(self, response):
        print(f'\U0001F3BE Returning random compliment to chat')
        compliment = self.compliments[random.randrange(0, len(self.compliments)-1)]
        return self.commandType + " #toerktumlare :" + compliment