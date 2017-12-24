import requests
import json
import time
import datetime
def getBoundingBox ( bBoxName ):
    if bBoxName == 'Hollywood':
        bboxqs = "?fEBnd=-87.66&fWBnd=-87.679&fSBnd=41.949&fNBnd=42.019"
    elif bBoxName == 'OHare':
        bboxqs = "?fEBnd=-87.807414&fWBnd=-88.8024212&fSBnd=41.907635&fNBnd=42.048809"
    elif bBoxName == 'Midway':
        bboxqs = "?fWBnd=-87.8641&fEBnd=-87.703&fSBnd=41.749&fNBnd=41.836"
    return bboxqs
baseurl = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json'
url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json' \
     '?fEBnd=-87.66&fWBnd=-87.679&fSBnd=41.949&fNBnd=42.019&lat=41.9857012&lng=-87.671544'
#Landing at O'Hare from the East
url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json' \
     '?fEBnd=-87.807414&fWBnd=-88.8024212&fSBnd=41.907635&fNBnd=42.048809&fAltU=5000&fAltL=500'
url = baseurl + \
      getBoundingBox('OHare') + "&fAltU=5000&fAltL=100"
while True:
    r = requests.get(url)
    z = json.loads(r.content)
    x = z["totalAc"]
    #print(x)
    y = z["acList"]
    nRow = len(y)
    if nRow>0:
        for nRowNum in range(0,nRow):
            if y[nRowNum].get("Man","") != "":
                print(y[nRowNum].get("Call","")+"\t"
                                                "\t"+
                y[nRowNum].get("Man","")+"\t\t"+
                y[nRowNum].get("Type","")+"\t\t"+
                y[nRowNum].get("Mdl","")+"\t\t"+
#                str(y[nRowNum].get("PosTime",""))+"\t" +
		str(datetime.datetime.now().time())[0:8]+"\t"+
#                time.strftime('%m/%d/%Y %H:%M:%S', time.gmtime(y[nRowNum].get("PosTime","") / 1000.)) + "\t" +
                str(y[nRowNum].get("Alt",""))+"\t" +
                str(y[nRowNum].get("Lat",""))+"\t" +
                str(y[nRowNum].get("Long",""))+"\t" +
                      str(y[nRowNum].get("Year", "")) + "\t" +
                      str(y[nRowNum].get("Trak", "")) + "\t" +
                str(y[nRowNum].get("Dst", ""))
                )
    time.sleep(10)




