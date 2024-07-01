import serial

def location():
    location = []

    #port name might be serial num
    #serial num: X000VXN2QV

    portName = "X000VXN2QV"
    
    while True:
        gps = serial.Serial(portName, 9600)
        gps_raw_data = gps.readline()
        gps_data = gps_raw_data.decode("utf-8")
        gps_list = gps_data.split(",")
        if gps_list[0] == "$GPGGA":
            lat = gps_list[2]
            latS = lat[0:lat.index('.')]
            lat = latS[0:(len(latS) - 2)] + ' ' + latS[(len(latS) - 2):len(latS)] + "." + lat[(lat.index('.') + 1): len(lat)]
            lon = gps_list[4]
            lonS = lon[0:lon.index('.')]
            lon = lonS[0:(len(lonS) - 2)] + ' ' + lonS[(len(lonS) - 2):len(lonS)] + "."  + lon[(lon.index('.') + 1): len(lon)]
            location = [lat, lon]
        break
    return location

def location(x):
    list = ["30.289790, -97.741344", "30.289729, -97.740541", "30.289692, -97.740280", "30.286547, -97.738484"]
    return list[x]
