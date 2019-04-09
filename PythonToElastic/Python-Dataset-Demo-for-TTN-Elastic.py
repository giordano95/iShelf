# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:05:04 2019

@author: Francesco
"""
import numpy as np
import pandas as pd
import random as rand


index_name = 'ishelf'
global_index = 90
supermarkets = ['COOP - ROME', 'COOP - MILAN', 'COOP - NAPOLI', 'COOP - PALERMO', 'COOP - TURIN']
products = ['Coca Cola', 'Pepsi']
max_product_for_store = 100
dataset = []
quantities = rand.randint(0, max_product_for_store)


def sell_timeline (quantity):
    start = pd.Timestamp(2019, 8, 4, 8)
    end = pd.Timestamp(2019, 8, 4, 21)
    #print (start)
    timeline = np.linspace(start.value, end.value, quantity)
    timeline= pd.to_datetime(timeline, format='%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%dT%H:%M:%S')
    #timeline= pd.to_datetime(timeline, format='%Y-%m-%d %H:%M:%S.%f')
    #timeline= pd.to_datetime(timeline)
    return timeline

def sell_istant (quantity):
    start = 1
    end = 1000
    #print (start)
    timeline_istant = np.linspace(start, end, quantity, dtype = int)
    return timeline_istant



t = sell_timeline (quantities)
t_istant = sell_istant (quantities)

product = products[1]
supermarket = supermarkets[1]
remains_product = quantities

for z in range (quantities):
    #document = '{ "index" : { "_index" : "' + index_name + '", "_type" : "json" } }\n{"product":"' + product + '","supermarket":"' + supermarket + '","date":"' + str(t[z]) + '","quantity":' + str(remains_product) + '}'
    document = {"product": product, "supermarket": supermarket ,"timestamp": str(t[z]), "time_istant": str(t_istant[z]), "quantity": str(remains_product) }
    global_index = global_index + 1
    remains_product = remains_product - 1
    #dataset.append (document)
    print (document)

print ('Perfect: you have created ' + str(quantities) + ' documents for Elastic!')
