import math
import argparse
import sys
import os

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-x', '--koord_x', default='0')
    parser.add_argument ('-y', '--koord_y', default='0')
    parser.add_argument ('-z', '--zoom', default='15')
    return parser

if __name__ == '__main__':
    parser = createParser()
    space_param = parser.parse_args(sys.argv[1:])
    x_tile,y_tile = deg2num(float(space_param.koord_y),float(space_param.koord_x),float(space_param.zoom))
    wget_text = 'wget http://tile.osm.org/'+str(space_param.zoom)+'/'+str(x_tile)+'/'+str(y_tile)+'.png'
    print (wget_text)
    os.system(wget_text)
    print (x_tile)
