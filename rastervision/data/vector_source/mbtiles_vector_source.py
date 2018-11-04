import json
from subprocess import Popen, PIPE, check_output
import logging
import os

from supermercado.burntiles import burn
from shapely.geometry import shape

from rastervision.data.vector_source.vector_source import VectorSource
from rastervision.utils.files import download_if_needed, get_local_path
from rastervision.rv_config import RVConfig

log = logging.getLogger(__name__)


def mbtiles_to_geojson(uri, crs_transformer, extent):
    log.info('Downloading and converting vector tiles to GeoJSON...')

    # Get all tiles covering extent.
    map_extent = extent.reproject(
        lambda point: crs_transformer.pixel_to_map(point))
    extent_polys = [{
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": [map_extent.geojson_coordinates()]
        }
    }]
    # TODO make zoom an option
    zoom = 12
    xyzs = burn(extent_polys, zoom)

    # Download tiles and convert to geojson.
    # Convert to Geojson.
    features = []
    for xyz in xyzs:
        x, y, z = xyz
        tile_uri = uri.format(x=x, y=y, z=z)
        with RVConfig.get_tmp_dir() as tmp_dir:
            tile_path = download_if_needed(tile_uri, tmp_dir)
            cmd = ['tippecanoe-decode', tile_path, str(z), str(x), str(y)]
            tile_geojson_str = check_output(cmd).decode('utf-8')
            tile_features = json.loads(tile_geojson_str)
            tile_features = tile_features['features'][0]['features']
            features.extend(tile_features)

    # TODO Merge features.
    geojson = {
        'type': 'FeatureCollection',
        'features': features
    }
    return geojson


class MBTilesVectorSource(VectorSource):
    def __init__(self,
                 uri,
                 crs_transformer,
                 extent,
                 class_map=None,
                 class_id_to_filter=None):
        self.uri = uri
        self.crs_transformer = crs_transformer
        self.extent = extent
        super().__init__(
            class_map=class_map, class_id_to_filter=class_id_to_filter)

    def _get_geojson(self):
        return mbtiles_to_geojson(self.uri, self.crs_transformer, self.extent)
