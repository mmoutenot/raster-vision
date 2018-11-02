# Copied from https://github.com/developmentseed/label-maker/blob/master/label_maker/stream_filter.py
# flake8: noqa

"""Filter streaming geojson by a bounding box"""
import sys
import json
from shapely.geometry import shape, box

bbox = box(*json.loads(sys.argv[1]))

for line in sys.stdin:
    geo = json.loads(line)
    geom = shape(geo['geometry'])
    geo.pop('tippecanoe')
    if bbox.intersects(geom):
        sys.stdout.write(json.dumps(geo) + '\n')
