from commands.ping import Ping
from commands.twitch_ping import TwitchPing
from commands.command_types import CommandType
from commands.random_number import RandomNumber
from commands.compliment import Compliment
from commands.commands import Commands

def getCommandList():
    return { 
            TwitchPing("PING", CommandType.PONG),
            Ping("!ping", CommandType.PRIVMSG),
            RandomNumber("!random", CommandType.PRIVMSG),
            Compliment("!compliment", CommandType.PRIVMSG),
            Commands("!commands", CommandType.PRIVMSG)
        }
