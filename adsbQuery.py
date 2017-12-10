import requests
import json
import time
import datetime
from enum import Enum

#class boundingBoxType (Enum):
 #   Hollywood=1
  #  Ohare=2
   # Midway=3
def getBoundingBox ( bBoxName ):
    if bBoxName=='Hollywood':
        bboxqs = "?fEBnd=-87.66&fWBnd=-87.679&fSBnd=41.949&fNBnd=42.019"
    return bboxqs
#import json2html
#import json2table
#Here is an extra comment
# Latitude runs east and west
# Longitude runs north and south
#url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=41.985271&long=-87.671491'
#url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?lat=41.985271&long=-87.671491&fDstL=0&fDstU=1000&fAltU=5000&fAltL=1000'
#url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?fAir=ORD&fAltU=5000&fAltL=1000'
baseurl = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json'
url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json' \
     '?fEBnd=-87.66&fWBnd=-87.679&fSBnd=41.949&fNBnd=42.019&lat=41.9857012&lng=-87.671544'
#Landing at O'Hare from the East
url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json' \
     '?fEBnd=-87.66&fWBnd=-87.679&fSBnd=41.949&fNBnd=42.019&fAltU=5000&fAltL=500'
url = baseurl + \
      getBoundingBox('Hollywood') + "&fAltU=5000&fAltL=500"




print(getBoundingBox('Hollywood'))
#Landing at Midway
#url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json' \
 #    '?fWBnd=-87.8641&fEBnd=-87.703&fSBnd=41.749&fNBnd=41.836&fAltU=5000&fAltL=500'
#url = 'http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json'

#print("Length of acList dictionary:\t" + str(nRow))
#print(y[1])
#print("Manu\tType\tModel\tAlt\tDst\tFrom\tTo")
#print(str(datetime.datetime.now().time())[0:8])
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
    #print(y[nRow]["Type"])
#print(z)
#print (y['Mdl'])
#print(z['acList'])
#print(json2table.convert(r.content))




