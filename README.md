# iShelf
IOT Inventory Management


## Why TheThingsNetwork?

One of the first and stable projects for IOT networks based on LoRaWAN is represented by TheThingsNetwork. As LoRaWAN is not an IP protocol we need this network to send messages that come out from the device to the desired application. That’s why TheThingsNetwork is between the gateways and the applications.

## How does TTN work?

Routing operations are all executed in a distributed and decentralized way. This allows to perform either local or global implementations. Messages are sent through the LoRa protocol and they can be of three different types:
-	A (rarely sending data)
-	B (regularly receiving data)
-	C (constantly receiving data)

The gateway is a device that receives LoRa messages and sends them to the router. Router is a microservice that is responsible of the gateway state and of the transmission scheduling. Each router is connected to one or more brokers that represent the heart of TTN. The broker is a microservice that identifies the device, performs some processing on data and sends the packet to the relative application’s handler. It is very important because it associates a specific device with a specific application and sends uplink messages to the correct receiver.  The handler is a microservice that is responsible of the data management within the applications and it also performs AES decrypt/encrypt operations.
The number of gateways is also important because more gateways mean more scalability.

In order to connect a device to TheThingsNetwork we need to add it to the console. The registration is very simple and the majority of the settings are randomly generated. One of the most important things to remember is that TTN allows us to use two different activation methods for our devices. One is OTAA and the other one is ABP. The main difference between the two is that OTAA uses dynamic keys while ABP keys are inserted manually by the user in the code of the board. This technique is obviously more practical but there are some security issues to face.

Once the board is connected to TTN, communication starts and sent packets are visualized on TTN through the Data panel. This panel gives us some information about the sender and the message. The payload of the message is Hex encrypted, but an ASCII translation is also proposed. The message is decoded following the instructions of the payload format, that is nothing more than a JSON file.     

As we have previously said, TTN is just used to route the packets in the network and so we are also interested in knowing how to come out from it. To do so, there is a TTN integration that is called HTTP integration. It simply forward packets to the desired server through the usage of HTTP protocol. As our server needs a login to be used, it was necessary to add to the server URL, also the connection parameters such as username and password. This is done by clearly writing them at the beginning of the URL separated by an at symbol. Obviously this choice can cause security issues but for our demo is not relevant at the moment.

In this way all the packets that we receive on TTN are automatically sent to our server. In this specific case, our server is ElasticSearch that is a distributed database that works with Kibana visualizer to show us some graphs about our application. 
