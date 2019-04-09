# iShelf
IOT Inventory Management

Internet Of Things Mini Project - Sapienza University of Rome

April 2019

## Why TheThingsNetwork?

One of the first and most stable projects for IOT networks based on LoRaWAN is represented by TheThingsNetwork. As LoRaWAN is not an IP protocol we need this network to send messages that come out from the device to the desired application. That’s why TheThingsNetwork is between the gateways and the applications.

## How does TTN work?

Routing operations are all executed in a distributed and decentralized way. This allows to perform either local or global implementations. Messages are sent through the LoRa protocol and they can be of three different types:
-	A (rarely sending data)
-	B (regularly receiving data)
-	C (constantly receiving data)

The gateway is a device that receives LoRa messages and sends them to the router. Router is a microservice that is responsible of the gateway state and of the transmission scheduling. Each router is connected to one or more brokers that represent the heart of TTN. The broker is a microservice that identifies the device, performs some processing on data and sends the packet to the relative application’s handler. It is very important because it associates a specific device with a specific application and sends uplink messages to the correct receiver.  The handler is a microservice that is responsible of the data management within the applications and it also performs AES decrypt/encrypt operations.
The number of gateways is also important because more gateways mean more scalability.

In order to connect a device to TheThingsNetwork we need to add it to the console. The registration is very simple and the majority of the settings are randomly generated. One of the most important things to remember is that TTN allows us to use two different activation methods for our devices. One is OTAA and the other one is ABP. The main difference between the two is that OTAA uses dynamic keys while ABP keys are inserted manually by the user in the code of the board. This technique is obviously more practical but there are some security issues to face.

Once the board is connected to TTN, communication starts and sent packets are visualized on TTN through the Data panel. This panel gives us some information about the sender and the message. The payload of the message is Hex encrypted, but an ASCII translation is also proposed. The message is decoded following the instructions of the payload format, that is nothing more than a JSON file.     

As we have previously said, TTN is just used to route the packets in the network and so we are also interested in knowing how to come out from it. To do so, there is a TTN integration that is called HTTP integration. It simply forward packets to the desired server through the usage of HTTP protocol. As our server needs a login to be used, it was necessary to add to the server URL, also the connection parameters such as username and password. This is done by clearly writing them at the beginning of the URL and by separating them with an "@" symbol. Obviously this choice can cause security issues but for our demo is not relevant at the moment.

In this way all the packets that we receive on TTN are automatically sent to our server. In this specific case, our server is ElasticSearch that is a distributed database that works with Kibana visualizer to show us some graphs about our application.



## H2 Elastic and Kibana 

### H3 Info about Elastic

Some technical (but useful) information to know about Elasticsearch are:
It is a real time distributed and analytics engine.
It is open source, developed in Java.
It uses an structure based in documents instead of tables and schema.
Elasticsearch is very useful for big data, making it easy to analyse million of data in almost real time searches.
In order to search all these datas you hve to use queries.
Query: The language to perform and combine many types of searches like structured, unstructured, geo, metric, etc. You can ask a query “anyway you want”.
And about analysis, Elasticsearch lets you understand billions of log lines easily. It provides aggregations which help you zoom out to explore trends and patterns in your data.
For example, if you have a cloud with 1000 nodes, you can analyse the entire infrastructure in a short period of time, importing the logs into Elasticsearch and, based on it’s response, you can get to the root cause of an issue in your infrastructure.

Elasticsearch is used from a very famous clients: for example Mozilla, GitHub, Stack Exchange, Netflix, and many more users.
Another important feature of Elastic is its Kibana, a great web interface to visualize and manipulate the data.
It can be downloaded in elastic.co and installed following few simple steps.
You need to download the same version for Elasticsearch and Kibana.
When, in the future, will find yourself needing to develop a software to interact with Elasticsearch, you can use a programming language to interact with it. Some of the programming languages acceptable are:
Java, C#, Python, JavaScript, PHP, Perl, Ruby

## H2 Create an Elastic Demo Dataset with Python
To test better Elastic my work has been foculised on create a demo dataset to use to study both Elastic and Kibana.
As we said previous, it's possible load data with Rest method (url method) for example using a simple interface as PostMan.
Rest is the method that we use to connect our device iShell trought TTN until Elastic.
Anyway there ohter methods: for example the Dev Tools under Kibana or API tools Under Elastic interface.

But it's also possible connect Python with Elastic to save documents.
This is a very powerful possibility beacause we can create a lot of data and configure as we want our index under Elastic.

The first thing to do is to install Elastic library for Python


Now we can connect with Elastic through few simple lines:

```python
# Import Elasticsearch package 
from elasticsearch import Elasticsearch 

# Connect to the elastic cluster
es=Elasticsearch([{'host':'localhost','port':9200}])  
```

Creation of several variables to configure in depth a very diversified documents.
We work for to put inside quantity from a shelf, but in the real world we will possible change and add many different other data through this program.

```python
index_name = 'ishelf'
global_index = 90
supermarkets = ['COOP - ROME', 'COOP - MILAN', 'COOP - NAPOLI', 'COOP - PALERMO', 'COOP - TURIN']
products = ['Coca Cola', 'Pepsi']
max_product_for_store = 100
dataset = []
quantities = rand.randint(0, max_product_for_store)
```

Which are the most important and difficult data to put inside Elastic? Time series.
Through sell_timeline it's possibile create a linspace timeline. 
The most important thing is the formattation of date.
Infact Elastic is programmed to recognize date timestamp if this has a particular structure.
Otherways it will insert a normale text data.

```python
def sell_timeline (quantity):
    start = pd.Timestamp(2019, 8, 4, 8)
    end = pd.Timestamp(2019, 8, 4, 21)
    #print (start)
    timeline = np.linspace(start.value, end.value, quantity)
    timeline= pd.to_datetime(timeline, format='%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%dT%H:%M:%S')
    #timeline= pd.to_datetime(timeline, format='%Y-%m-%d %H:%M:%S.%f')
    #timeline= pd.to_datetime(timeline)
    return timeline
```

The last part of program create the string to send to Elastic
The instruction es.index insert document in the index and in the type we have choosen.
For the index_id is possibile to indicate also it, or leave blank thi field and Elastic make an automatic insertion.

```python
for z in range (quantities):
    #document = '{ "index" : { "_index" : "' + index_name + '", "_type" : "json" } }\n{"product":"' + product + '","supermarket":"' + supermarket + '","date":"' + str(t[z]) + '","quantity":' + str(remains_product) + '}'
    document = {"product": product, "supermarket": supermarket ,"timestamp": str(t[z]), "time_istant": str(t_istant[z]), "quantity": str(remains_product) }
    global_index = global_index + 1
    remains_product = remains_product - 1
    res = es.index(index= index_name, doc_type='shelf',id=global_index,body=document)
    #dataset.append (document)
    print (document)
```
