from .base_command import BaseCommand

class Ping(BaseCommand):
    def __init__(self, command):
        super().__init__(command)

    def is_match(self):
        return super().is_match()

    def process(self):
        return "PONG"
