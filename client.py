#!/usr/bin/env python

import asyncio
import websockets
import ssl
import argparse

from commands.ping import Ping
from commands.command_utils import getCommandList

class Client:
  def __init__(self, uri, token, nick, channel):
    self.uri = uri
    self.token = token
    self.nick = nick
    self.channel = channel
    self.commands = getCommandList()

  def __process(self, chatResponse):
    for command in self.commands:
      if(command.is_match(chatResponse)):
        return command.execute(chatResponse)
    return None

  async def __start_loop(self, websocket):
    while True:
      chatResponse = await websocket.recv()
      print(f"< {chatResponse}", end='')
      response = self.__process(chatResponse)
      print(f'{response}')
      if(response is not None):
        await websocket.send(response)

  async def Start(self):
    token = "PASS " + "oauth:" + self.token
    nick = "NICK " + self.nick
    channel = "JOIN #" + self.channel
    print("\U00002705	Connecting to Twitch")
    async with websockets.connect(self.uri) as websocket:
    
      await websocket.send(token)
      await websocket.send(nick)
      response = await websocket.recv()
      print(f'{response}')
      await websocket.send(channel)
      response = await websocket.recv()
      print(f'{response}')
      await self.__start_loop(websocket)

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

  print("\U0001F4BB	Starting client")
  client = Client(uri, token, nick, channel)
  asyncio.run(client.Start())

if __name__ == "__main__": 
  main()