# usage $ python src/ydf_to_geojson.py > udon.json
import urllib
import json
from geojson import Feature, Point, FeatureCollection
import pprint

appid = ''
url = 'https://map.yahooapis.jp/search/local/V1/localSearch?appid='+appid+'&ac=37&query=%E3%81%86%E3%81%A9%E3%82%93&output=json&results=100'
ydf = json.load(urllib.urlopen(url))

feature_list = []
for feature in ydf['Feature']:
    ll = feature['Geometry']['Coordinates'].split(',')
    point = Point((float(ll[0]), float(ll[1])))
    link = 'https://loco.yahoo.co.jp/place/' + feature['Gid'] + '/'
    feature_list.append(Feature(geometry=point, properties={'title' : feature['Name'], 'link' : link}))

print FeatureCollection(feature_list)

