import ephem
import random
from math import degrees
from datetime import datetime

place = ephem.Observer()
place.lat = '31.7754'
place.lon = '76.9861'
place.elevation = 1000
place.date = datetime.now().date().strftime('%Y/%m/%d')


# print (datetime.now().date().strftime('%Y/%m/%d'))

test_place = place

ra_req = input("Enter the ra:  ")
dec_req = input("Enter the dec:  ")
m45 = ephem.FixedBody()
m45.name = "M 45"
#m45._ra = '3:47:24.0'
#m45._dec = '24:7:0.0'
m45._ra = ra_req
m45._dec = dec_req
# jupiter = ephem.Jupiter()
# jupiter.compute(test_place)

test_place.date = ephem.now()
m45.compute(test_place)
# print (m45.name)
print ("Resultant Altitude: "degrees(m45.alt)) 
print ("Resultant Azimuth: "degrees(m45.az)) 

# print (jupiter.name)
# print (degrees(jupiter.alt)) 
# print (degrees(jupiter.az)) 
