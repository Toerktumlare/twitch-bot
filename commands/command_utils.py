from commands.ping import Ping
from commands.twitch_ping import TwitchPing
from commands.command_types import CommandType
from commands.dice import Dice
from commands.compliment import Compliment
from commands.commands import Commands

def getCommandList(channel):
    return { 
            TwitchPing("PING", CommandType.PONG),
            Ping("!ping", CommandType.PRIVMSG, channel),
            Dice("!dice", CommandType.PRIVMSG, channel),
            Compliment("!compliment", CommandType.PRIVMSG, channel),
            Commands("!commands", CommandType.PRIVMSG, channel)
        }
