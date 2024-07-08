import serial

def location():
    location = []
    gps = serial.Serial("com6", 9600)
    while True:
        gps_raw_data = gps.readline()
        gps_data = gps_raw_data.decode("utf-8")
        gps_list = gps_data.split(",")
        if gps_list[0] == "$GPGGA":
            lat = gps_list[2]
            if (lat == "") == False:
                latS = lat[0:lat.index('.')]
                latDD = latS[0:(len(latS) - 2)]
                if gps_list[3] == 'S':
                    latDD = "-" + latDD
                lat = latDD + ' ' + latS[(len(latS) - 2):len(latS)] + "." + lat[(lat.index('.') + 1): len(lat)]
                lon = gps_list[4]
                lonS = lon[0:lon.index('.')]
                lonDD = lonS[0:(len(lonS) - 2)]
                if gps_list[5] == 'W':
                    lonDD = "-" + lonDD
                lon = lonDD + ' ' + lonS[(len(lonS) - 2):len(lonS)] + "."  + lon[(lon.index('.') + 1): len(lon)]
                location = [lat, lon]
                break
    return location
