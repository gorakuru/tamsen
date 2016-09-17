#!/usr/bin/env python
# coding: utf-8
import json
import requests


def test():
    print 'foo'

def sendData(channel,writeKey,d1=0,d2=0,d3=0,d4=0,d5=0,d6=0,d7=0,d8=0):
	HOST = '54.65.206.59'
	response = requests.post(
      'http://'+HOST+'/api/v2/channels/'+str(channel)+'/data',
      json.dumps({'writeKey':writeKey,'d1':int(d1),'d2':int(d2),'d3':int(d3),'d4':int(d4),'d5':int(d5),'d6':int(d6),'d7':int(d7),'d8':int(d8)}),
      headers={'Content-Type': 'application/json'})
	return(response)