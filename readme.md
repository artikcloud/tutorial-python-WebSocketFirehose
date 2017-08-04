# Tutorial Python Firehose WebSocket

This is a starter code to connect to ARTIK Cloud [Firehose WebSocket (/live)](https://developer.artik.cloud/documentation/data-management/rest-and-websockets.html#firehose-websocket) endpoint.   By running this sample you will learn to:

- Connect to the ARTIK Cloud Firehose WebSocket url.
- Monitor realtime messages sent to ARTIK Cloud by the specified source device.

Consult [Python device channel WebSocket](https://github.com/artikcloud/tutorial-python-WebSocketDevicechannel) for how to use device channel WebSocket.

Consult [An IoT remote control](https://developer.artik.cloud/documentation/tutorials/an-iot-remote-control.html#develop-an-android-app) for how to develop an Android monitor app.

## Requirements

- [Python3](https://www.python.org/downloads/) >= 3.5
- [pip3](https://pypi.python.org/pypi/pip) >= 9.0


## Setup

### Setup at ARTIK Cloud

- Go to the Devices Dashboard (https://my.artik.cloud) and [add a new device](https://developer.artik.cloud/documentation/tools/web-tools.html#connecting-a-device):

  ```
  Device Type Name: Example Simple Smart Light
  Unique Name: cloud.artik.example.simple_smartlight
  ```

- Get the device ID for your newly created device in the [Device Info](https://developer.artik.cloud/documentation/tools/web-tools.html#managing-a-device-token) screen.

- Retrieve a [user token](https://developer.artik.cloud/documentation/tools/api-console.html#find-your-user-token) via api-console.   

### Setup Project

Before running the sample, fill in the following into your the `config.json` file:

```json
{
  "user_token": "YOUR-USER-TOKEN",
  "device_ids": "YOUR-DEVICE-ID"
}
```

In the next section you will install dependencies and run the project.   Verify you are using Python >= 3.5 before continuing.   For example, below output shows Python 3.6.

```
$ python3 --version
Python 3.6.0 

$ pip3 --version
pip 9.0.1 from /usr/local/lib/python3.6/site-packages (python 3.6)
```

Install dependencies with following command:

 ```bash
$ pip3 install websockets
 ```

##### Run Project

```bash
$ python3 monitor.js
```

## Demo:

1. After running the project, your terminal output will look like the following.   A WebSocket connection is open and will output any messages that are sent to the device.

```bash
$ python3 monitor.js 
Connecting to:  wss://api.artik.cloud/v1.1/live?authorization=bearer+2fe4cd...&sdids=f32c7aa...
WebSocket connection is open ...
```

2. Send messages on behalf of your Example Simple Smart Light using the [Online Device Simulator](https://developer.artik.cloud/documentation/tools/web-tools.html#using-the-online-device-simulator).   This sample has the following settings:
   1. Simulate data on the boolean "state" field and keep the default interval to send every 5000 ms (5 secs).   
   2. Alternative between true/false value by setting the Data Pattern to Alternating Boolean.
3. Go back to your running sample application.   The terminal screen should output a message every 5 seconds:

```bash
$ python3 monitor.js 
Connecting to:  wss://api.artik.cloud/v1.1/live?authorization=bearer+2fe4cd...&sdids=f32c7aa...
WebSocket connection is open ...

Received message with data: {"mid":"b6967f3fb42144c58ecce19bef2087d1","data":{"state":true},"ts":1501201750000,"boid":"dfef0b21074349f79aaf6081c7865e7d","sdtid":"dtd1d3e0934d9348b783166938c0380128","cts":1501201746746,"uid":"c58ecc...","mv":1,"sdid":"f32c7aa..."}

Received message with data: {"mid":"9d845aced605468990997f70cc11a2d0","data":{"state":false},"ts":1501201755000,"boid":"dfef0b21074349f79aaf6081c7865e7d","sdtid":"dtd1d3e0934d9348b783166938c0380128","cts":1501201752861,"uid":"c58ecc...","mv":1,"sdid":"f32c7aa..."}

Received message with data: {"mid":"207e8218da87403ba115f6df74b54775","data":{"state":true},"ts":1501201765000,"boid":"dfef0b21074349f79aaf6081c7865e7d","sdtid":"dtd1d3e0934d9348b783166938c0380128","cts":1501201762522,"uid":"c58ecc...","mv":1,"sdid":"f32c7aa..."}
```

4. Stop the simulation so it does not accrue any more data usage.


## More about ARTIK Cloud

If you are not familiar with ARTIK Cloud, we have extensive documentation at [https://developer.artik.cloud/documentation](https://developer.artik.cloud/documentation)

The full ARTIK Cloud API specification can be found at [https://developer.artik.cloud/documentation/api-spec.html](https://developer.artik.cloud/documentation/api-spec.html)

Peek into advanced sample applications at [https://developer.artik.cloud/documentation/samples/](https://developer.artik.cloud/documentation/samples/)

To create and manage your services and devices on ARTIK Cloud, visit the Developer Dashboard at [https://developer.artik.cloud](https://developer.artik.cloud/)

## License and Copyright

Licensed under the Apache License. See [LICENSE](./LICENSE).

Copyright (c) 2017 Samsung Electronics Co., Ltd.
