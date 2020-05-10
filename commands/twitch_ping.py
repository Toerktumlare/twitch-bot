from commands.base_command import BaseCommand

class TwitchPing(BaseCommand):
    def __init__(self, command):
        super().__init__(command)

    def is_match(self, response):
        if(response.startswith(self.command)):
            return True
        return False

    def execute(self, command):
        print("\U0001F3BE Responding to PING")
        return "PONG :tmi.twitch.tv"