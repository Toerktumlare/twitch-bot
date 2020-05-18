# twitch-bot
A small twitch bot written using python and the [Twitch irc api](https://dev.twitch.tv/docs/irc/guide).

## Prerequisites
- Python3 (at least version 3.4)
- Docker (if you want to build the docker image)
  
## How to run

Checkout this repo, then run main.py and supply the arguments _nickname_, _token_ and what _channel_ you want to join.

To easily get a valid token go to the [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi/) and attach your account.

Then run the app suppling the needed information.

Example:
```
$ python3 main.py <username> <token> <channel>
```

## Docker container
There is a Dockerfile in the root of this project. To build it just run the following command:

```
$ docker build .
```

## Usage

Currently the bot comes with some default example commands:

`!ping`

`!commands`

`!dice`

`!compliment`

## Implement custom command

Create a class in `commands` folder, inherit from the `BaseCommand` class, implement the two abstract methods `is_match` and `process` and you are good to go.

## TODO

- implement proper logging and debug logging flag
- implement specific mod commands
- implement a command that fetches something from a random rest api
