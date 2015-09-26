plate_str = "JMW{}"
car_make = "LEXUS"
car_type = "RX"
state = "PA"
from pyquery import PyQuery as pq

from requests import get
from time import sleep


url = "http://www.carfax.com/processQuickVin.cfx?partnerCode=CFX&partnerSiteLocation=Y&checkReport=DEC&checkReportVersion=30&fid=&test=&cctest=&affiliateId=&subId=&bannerName=&partnerCode=CFX&partnerSiteLocation=Y&checkReport=DEC&checkReportVersion=30&fid=&test=&cctest=&affiliateId=&subId=&bannerName=&licensePlateNumber={}&licensePlateState={}"


def plate_string_gen():

    for i in (xrange(534,10000)):
    	print i
        r = get(url.format(plate_str.format(str(i).zfill(4)), "PA"))
        d = pq(r.content)
        info = d(".vehicleInfo").text()
        print info
        if car_make in info and car_type in info:
            print info
            print i
            raise BaseException
        

plate_string_gen()