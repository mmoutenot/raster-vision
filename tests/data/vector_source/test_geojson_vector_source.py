import unittest
import json
import os

from rastervision.data.vector_source import (GeoJSONVectorSourceConfigBuilder,
                                             GeoJSONVectorSourceConfig)
from rastervision.data.vector_source.class_transformer import ClassTransformer
from rastervision.core.class_map import ClassMap
from rastervision.utils.files import str_to_file
from rastervision.rv_config import RVConfig


class TestGeoJSONVectorSource(unittest.TestCase):
    """This also indirectly tests the ClassTransformer."""
    def setUp(self):
        self.class_map = ClassMap.construct_from(['building', 'car'])
        self.class_id_to_filter = {
            1: ['==', 'type', 'building'],
            2: ['any', ['==', 'type', 'car'], ['==', 'type', 'auto']]
        }
        self.class_transformer = ClassTransformer(self.class_map,
                                                  self.class_id_to_filter)

        # This should hit the 4 ways of inferring a class_id.
        self.geojson = {
            'type':
            'FeatureCollection',
            'features': [{
                'properties': {
                    'class_id': 3
                }
            }, {
                'properties': {
                    'label': 'car'
                }
            }, {
                'properties': {
                    'type': 'auto'
                }
            }, {}]
        }

        self.temp_dir = RVConfig.get_tmp_dir()
        self.uri = os.path.join(self.temp_dir.name, 'vectors.json')
        str_to_file(json.dumps(self.geojson), self.uri)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_transform_geojson(self):
        b = GeoJSONVectorSourceConfigBuilder() \
            .with_class_filters(self.class_id_to_filter) \
            .with_uri(self.uri) \
            .build()

        config = GeoJSONVectorSourceConfig.from_proto(b.to_proto())
        source = config.create_source(class_map=self.class_map)

        transformed_geojson = source.get_geojson()
        expected_transformed_geojson = {
            'type':
            'FeatureCollection',
            'features': [{
                'properties': {
                    'class_id': 3
                }
            }, {
                'properties': {
                    'label': 'car',
                    'class_id': 2
                }
            }, {
                'properties': {
                    'type': 'auto',
                    'class_id': 2
                }
            }, {
                'properties': {
                    'class_id': 1
                }
            }]
        }

        self.assertDictEqual(transformed_geojson, expected_transformed_geojson)


if __name__ == '__main__':
    unittest.main()
