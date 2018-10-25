from abc import abstractmethod
from copy import deepcopy

from google.protobuf import (json_format)

import rastervision as rv
from rastervision.core.config import Config, ConfigBuilder
from rastervision.protos.vector_source_pb2 import (VectorSourceConfig as
                                                   VectorSourceConfigMsg)


class VectorSourceConfig(Config):
    def __init__(self, source_type, class_id_to_filter=None):
        self.source_type = source_type
        self.class_id_to_filter = class_id_to_filter

    def to_proto(self):
        msg = VectorSourceConfigMsg(source_type=self.source_type)

        if self.class_id_to_filter is not None:
            # Convert class_ids to str to put into json format.
            class_id_to_filter = dict(
                [(str(class_id), filter)
                 for class_id, filter in self.class_id_to_filter.items()])
            d = {'class_id_to_filter': class_id_to_filter}
            msg.MergeFrom(json_format.ParseDict(d, VectorSourceConfigMsg()))

        return msg

    @staticmethod
    def builder(source_type):
        return rv._registry.get_config_builder(rv.VECTOR_SOURCE, source_type)()

    def to_builder(self):
        return rv._registry.get_config_builder(rv.VECTOR_SOURCE,
                                               self.source_type)(self)

    @staticmethod
    def from_proto(msg):
        """Creates a from the specificed protobuf message.
        """
        return rv._registry.get_config_builder(rv.VECTOR_SOURCE, msg.source_type)() \
                           .from_proto(msg) \
                           .build()

    @abstractmethod
    def create_source(self, crs_transformer=None, extent=None, class_map=None):
        pass


class VectorSourceConfigBuilder(ConfigBuilder):
    def from_proto(self, msg):
        b = self
        d = json_format.MessageToDict(msg)
        if msg.HasField('class_id_to_filter'):
            # Convert class_ids from strs to ints.
            # Have to use camel case after parsing from json :(
            class_id_to_filter = dict(
                [(int(class_id), filter)
                 for class_id, filter in d['classIdToFilter'].items()]
            )
            b = b.with_class_filters(class_id_to_filter)

        return b

    def with_class_filters(self, class_id_to_filter):
        b = deepcopy(self)
        b.config['class_id_to_filter'] = class_id_to_filter
        return b
