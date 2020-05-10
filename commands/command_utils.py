from commands.ping import Ping
from commands.twitch_ping import TwitchPing

def getCommandList():
    return { 
            TwitchPing("PING"),
            Ping("!ping") 
        }
