# usage $ python src/ydf_to_geojson.py > udon.json
import urllib
import json
from geojson import Feature, Point, FeatureCollection
import pprint

def append_feature (ydf):    
    for feature in ydf['Feature']:
        ll = feature['Geometry']['Coordinates'].split(',')
        point = Point((float(ll[0]), float(ll[1])))
        link = 'https://loco.yahoo.co.jp/place/g-' + feature['Gid'] + '/'
        feature_list.append(Feature(geometry=point, properties={'title' : feature['Name'], 'link' : link}))

feature_list = []
appid = ''
url = 'https://map.yahooapis.jp/search/local/V1/localSearch?appid='+appid+'&ac=37&gc=0101018&output=json&results=100&start='

ydf = json.load(urllib.urlopen(url))
append_feature(ydf)

refetch_num = ydf['ResultInfo']['Total'] / 100
for i in range(refetch_num):
    start = 100*(i+1)+1
    append_feature(json.load(urllib.urlopen(url+str(start))))

print FeatureCollection(feature_list)
