from commands.base_command import BaseCommand

class Ping(BaseCommand):
    def __init__(self, command):
        super().__init__(command)

    def is_match(self, response):
        str_array = response.split(":")
        print(f'{str_array}')
        if(str_array[2].rstrip() == self.command):
            return True
        return False

    def execute(self, response):
        print(f'\U0001F3BE Ponging back to chat')
        return "PRIVMSG #toerktumlare :PONG"
