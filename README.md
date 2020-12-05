# twitbug

Scrape tweets from mobile.twitter.com for a given user. Grabs 5 initially and then polls for new ones every 10 mins. Can curl server address for a JSON dump of tweets. Also optionally run it in Docker.

NOTE: This API is being killed off on 15 December 2020.

## Setup

`pip install -r requirements.txt`

## Running

`python3 twitbug.py <twitter-handle> <server-address> <server-port>`

E.g. `python3 twitbug.py Twitter 127.0.0.1 8888`

## Requesting JSON dump of all collected tweets

Using the example above:

`curl http://127.0.0.1:8888/`

## Docker

Build container:

`docker build -t twitbug:latest .`

Run the container (attached, see output in terminal):

`docker run --rm -p 127.0.0.1:8888:8888/tcp -e HANDLE=<handle> --name twitbug twitbug`

Run the container (detached, see output using docker logs):

`docker run --rm -d -p 127.0.0.1:8888:8888/tcp -e HANDLE=<handle> --name twitbug twitbug`
