import requests
import json
import time
import datetime
################################################################################################
###############################  getBoundingBox ################################################
################################################################################################
def getBoundingBox ( bBoxName ):
    if bBoxName == 'Hollywood':
        bboxqs = "?fEBnd=-87.66&fWBnd=-87.679&fSBnd=41.949&fNBnd=42.019"
    elif bBoxName == 'OHare':
        bboxqs = "?fEBnd=-87.807414&fWBnd=-88.8024212&fSBnd=41.907635&fNBnd=42.048809"
    elif bBoxName == 'Midway':
        bboxqs = "?fWBnd=-87.8641&fEBnd=-87.703&fSBnd=41.749&fNBnd=41.836"
    return bboxqs
################################################################################################
###############################  main() ################################################
################################################################################################
baseurl = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json'
dispKeys = ['Call','Man','Type','Mdl','Alt','Lat','Long','Year','Trak','Dst']
dispKeys = ['Call','Man','Type','From','To','Alt','Lat','Trak','Dst']
wideBodyLeft3 = ['B78','B77','B76','B74','A30','A33','A34','A35','A38','MD1','DC1']
TAB_1 = "\t"
url = baseurl + getBoundingBox('OHare') + "&fAltU=5000&fAltL=100"
while True:
    r = requests.get(url)
    rjson = json.loads(r.content)
    #recs is a list of dictionaries.  Each dictionary is one aircraft.
    recs = rjson["acList"]
    nRow = len(recs)
    if nRow>0:
        for nRowNum in range(0,nRow):
            if recs[nRowNum].get("Type","") != "" and str(recs[nRowNum].get("Type",""))[0:3] in wideBodyLeft3:
                dispStr = str(datetime.datetime.now().time())[0:8]+TAB_1
                for thisKey in dispKeys:
                   dispStr = dispStr + str(recs[nRowNum].get(thisKey,""))+ TAB_1
                print(dispStr)
    time.sleep(10)




