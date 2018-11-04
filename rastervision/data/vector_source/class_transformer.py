import copy

from rastervision.data.vector_source.label_maker.filter import create_filter


class ClassTransformer():
    def __init__(self, class_map=None, class_id_to_filter=None):
        self.class_map = class_map
        self.class_id_to_filter = None

        if class_id_to_filter is not None:
            self.class_id_to_filter = {}
            for class_id, filter_exp in class_id_to_filter.items():
                self.class_id_to_filter[class_id] = create_filter(filter_exp)

    def infer_class_id(self, feature):
        # If class_id is present, use it.
        class_id = feature.get('properties', {}).get('class_id')
        if class_id is not None:
            return class_id

        if self.class_map is not None:
            # If class_name or label are present and in class_map, use corresponding
            # class_id.
            class_name = feature.get('properties', {}).get('class_name')
            if class_name in self.class_map.get_class_names():
                return self.class_map.get_by_name(class_name).id

            label = feature.get('properties', {}).get('label')
            if label in self.class_map.get_class_names():
                return self.class_map.get_by_name(label).id

        # If filter_fn is true when applied to feature, use corresponding class_id.
        if self.class_id_to_filter is not None:
            for class_id, filter_fn in self.class_id_to_filter.items():
                if filter_fn(feature):
                    return class_id
            return None

        # Default to class_id of 1.
        return 1

    def transform_geojson(self, geojson):
        new_features = []
        for feature in geojson['features']:
            class_id = self.infer_class_id(feature)
            if class_id is not None:
                feature = copy.deepcopy(feature)
                properties = feature.get('properties', {})
                properties['class_id'] = class_id
                feature['properties'] = properties
                new_features.append(feature)
        new_geojson = {
            'type': 'FeatureCollection',
            'features': new_features
        }
        return new_geojson
