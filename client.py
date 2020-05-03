#!/usr/bin/env python

import asyncio
import websockets
import ssl

async def send(uri, token, nick):

  token = "PASS " + "oauth:" + token
  nick = "NICK " + nick
  print("\U00002705	Connecting to Twitch")
  async with websockets.connect(uri) as websocket:
    
    await websocket.send(token)
    print(f"> {token}")
    await websocket.send(nick)
    print(f"> {nick}")
    response = await websocket.recv()
    print(f"< {response}")
    await websocket.send("JOIN #kandyland")
    while True:
      response = await websocket.recv()
      print(f"< {response}", end='')
      if response.startswith("PING"):
        print("\U0001F3BE Responding to PING")
        response = "PONG :tmi.twitch.tv"
        await websocket.send(response)
        print(f"< {response}")


def main():

  uri = "wss://irc-ws.chat.twitch.tv:443"
  token = "hexka0uz18q0s1aba6opg9spbc3baf"
  nick = "toerktumlare"

  print("\U0001F4BB	Starting client")
  asyncio.run(send(uri, token, nick))

if __name__ == "__main__": main()