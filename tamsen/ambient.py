#!/usr/bin/env python
# coding: utf-8
import json
import requests


def test():
    print 'foo'

def sendData(channel,writeKey,d1=None,d2=None,d3=None,d4=None,d5=None,d6=None,d7=None,d8=None):
	HOST = '54.65.206.59'
	data = {'writeKey':writeKey}
	if d1 is not None:
		data["d1"] = int(d1)
	if d2 is not None:
		data["d2"] = int(d2)
	if d3 is not None:
		data["d3"] = int(d3)
	if d4 is not None:
		data["d4"] = int(d4)
	if d5 is not None:
		data["d5"] = int(d5)
	if d6 is not None:
		data["d6"] = int(d6)
	if d7 is not None:
		data["d7"] = int(d7)
	if d8 is not None:
		data["d8"] = int(d8)	
	response = requests.post(
      'http://'+HOST+'/api/v2/channels/'+str(channel)+'/data',
      json.dumps(data),
      headers={'Content-Type': 'application/json'})
	return(response)