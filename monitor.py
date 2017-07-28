#!/usr/bin/env python

"""Sample WebSocket connection to ARTIK Cloud Firehose.

wss://api.artik.cloud/v1.1/live

Please see readme for more info:
https://github.com/artikcloud/tutorial-python-WebSocketFirehose/blob/master/readme.md

"""

import json
import sys
import asyncio
import websockets

with open('config.json') as json_data:
    CONFIG = json.load(json_data)


USER_TOKEN = CONFIG['user_token']
DEVICE_IDS = CONFIG['device_ids']
# Comma delimited string of device ids.

CONNECTION_URL = (
    'wss://api.artik.cloud/v1.1/live?authorization=bearer+{0}&sdids={1}'.format(USER_TOKEN, DEVICE_IDS)
    )

"""sample connection string

Example:
    wss://api.artik.cloud/v1.1/live?authorization=bearer+2fe4cd...&sdids=DEVICE_ID1,DEVICE_ID2

Documentation:
   https://developer.artik.cloud/documentation/api-reference/websockets-api.html#firehose-websocket


"""

async def consume_messages():
    """This function is called once from asyncio event loop.

    Once the websocket connection is established, it will print
    out any messages to console as messages are received.

    Example received message:

        > Received message with data:
        > {"mid":"b6967...", "data":{"state":true}, "ts":1501201750000, "sdid":"f32c7aa...",
            ... More}
        """

    print('\nConnecting to: ' + CONNECTION_URL)

    async with websockets.connect(CONNECTION_URL) as websocket:
        print('\nWebSocket connection is open ...')
        while True:
            message = await websocket.recv()
            print("\nReceived message with data: {}".format(message))

try:
    asyncio.get_event_loop().run_until_complete(consume_messages())
except KeyboardInterrupt as error:
    print("\nApplication Exited. {0}".format(error))
else:
    print("Unknown Error '{0}'".format(sys.exc_info()[0]))
