import unittest

from rastervision.data.vector_source import (MBTilesVectorSourceConfigBuilder,
                                             MBTilesVectorSourceConfig)
from rastervision.core.box import Box
from rastervision.core.class_map import ClassMap
from rastervision.data.crs_transformer import IdentityCRSTransformer


class TestMBTilesVectorSource(unittest.TestCase):
    def setUp(self):
        # This test file was copied from https://github.com/developmentseed/label-maker
        self.uri = '/opt/data/raw-data/germany/{z}/{x}/{y}.pbf'
        self.class_id_to_filter = {'1': ['has', 'building']}
        self.class_map = ClassMap.construct_from(['building'])
        self.crs_transformer = IdentityCRSTransformer()

        b = MBTilesVectorSourceConfigBuilder() \
            .with_class_filters(self.class_id_to_filter) \
            .with_uri(self.uri) \
            .build()

        self.config = MBTilesVectorSourceConfig.from_proto(b.to_proto())

    def test_get_geojson(self):
        # Should cover a few streets in Potsdam
        extent = Box.make_square(13.052637577056885, 52.4004812780123, 0.002)
        source = self.config.create_source(self.crs_transformer, extent,
                                           self.class_map)
        geojson = source.get_geojson()
        print(geojson)


if __name__ == '__main__':
    unittest.main()
