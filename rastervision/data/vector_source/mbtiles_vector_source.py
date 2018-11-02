import json
from subprocess import Popen, PIPE, check_output
import logging
import os

from rastervision.data.vector_source.vector_source import VectorSource
from rastervision.utils.files import download_if_needed, get_local_path
from rastervision.rv_config import RVConfig

log = logging.getLogger(__name__)


def mbtiles_to_geojson(uri, crs_transformer, extent):
    map_extent = extent.reproject(
        lambda point: crs_transformer.pixel_to_map(point))

    # Note we are using RVConfig.tmp_dir and not RVConfig.get_tmp_dir() because
    # we want this file to persist after this function exits for the sake of
    # caching.
    if RVConfig.tmp_dir is None:
        RVConfig.set_tmp_dir()
    tmp_root = RVConfig.tmp_dir
    mbtiles_dir = os.path.join(tmp_root, 'mbtiles')

    log.info('Converting MBTiles to GeoJSON...')
    path = get_local_path(uri, mbtiles_dir)
    if not os.path.isfile(path):
        path = download_if_needed(uri, mbtiles_dir)

    ps = Popen(['tippecanoe-decode', '-c', '-f', path], stdout=PIPE)
    filtered_geojson = check_output(
        [
            'python', '-m', 'rastervision.data.vector_source.label_maker.stream_filter',
            json.dumps(map_extent.shapely_format())
        ],
        stdin=ps.stdout).decode('utf-8')

    # Each line has a feature. The last line is empty so discard.
    features = [
        json.loads(feature) for feature in filtered_geojson.split('\n')[:-1]
    ]
    geojson = {'type': 'FeatureCollection', 'features': features}

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
