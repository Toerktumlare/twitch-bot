#!/usr/bin/env python

import asyncio
import websockets
import ssl
import argparse

from commands.ping import Ping

async def send(uri, token, nick, channel):

  token = "PASS " + "oauth:" + token
  nick = "NICK " + nick
  channel = "JOIN #" + channel
  print("\U00002705	Connecting to Twitch")
  async with websockets.connect(uri) as websocket:
    
    await websocket.send(token)
    print(f"> {token}")
    await websocket.send(nick)
    print(f"> {nick}")
    response = await websocket.recv()
    print(f"< {response}")
    await websocket.send(channel)
    print(f"< {channel}")
    while True:
      response = await websocket.recv()
      print(f"< {response}", end='')
      if response.startswith("PING"):
        print("\U0001F3BE Responding to PING")
        response = "PONG :tmi.twitch.tv"
        await websocket.send(response)
        print(f"< {response}")


def main():

  parser = argparse.ArgumentParser()
  parser.add_argument("nick", help="Twitch username")
  parser.add_argument("token", help="oauth token")
  parser.add_argument("channel", help="chat to connect to")

  args = parser.parse_args()

  uri = "wss://irc-ws.chat.twitch.tv:443"
  token = args.token
  nick = args.nick.lower()
  channel = args.channel

  ping = Ping("!ping")

  print("\U0001F4BB	Starting client")
  asyncio.run(send(uri, token, nick, channel))

if __name__ == "__main__": 
  main()