# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/label_source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rastervision.protos import raster_source_pb2 as rastervision_dot_protos_dot_raster__source__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from rastervision.protos import class_item_pb2 as rastervision_dot_protos_dot_class__item__pb2
from rastervision.protos import vector_source_pb2 as rastervision_dot_protos_dot_vector__source__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/label_source.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n&rastervision/protos/label_source.proto\x12\trv.protos\x1a\'rastervision/protos/raster_source.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a$rastervision/protos/class_item.proto\x1a\'rastervision/protos/vector_source.proto\"\xf7\x06\n\x11LabelSourceConfig\x12\x13\n\x0bsource_type\x18\x01 \x02(\t\x12`\n\x1dobject_detection_label_source\x18\x02 \x01(\x0b\x32\x37.rv.protos.LabelSourceConfig.ObjectDetectionLabelSourceH\x00\x12\x66\n chip_classification_label_source\x18\x03 \x01(\x0b\x32:.rv.protos.LabelSourceConfig.ChipClassificationLabelSourceH\x00\x12l\n#semantic_segmentation_raster_source\x18\x04 \x01(\x0b\x32=.rv.protos.LabelSourceConfig.SemanticSegmentationRasterSourceH\x00\x12\x30\n\rcustom_config\x18\x05 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x1aR\n\x1aObjectDetectionLabelSource\x12\x34\n\rvector_source\x18\x01 \x02(\x0b\x32\x1d.rv.protos.VectorSourceConfig\x1a\xf4\x01\n\x1d\x43hipClassificationLabelSource\x12\x34\n\rvector_source\x18\x01 \x02(\x0b\x32\x1d.rv.protos.VectorSourceConfig\x12\x12\n\nioa_thresh\x18\x02 \x01(\x02\x12\"\n\x1ause_intersection_over_cell\x18\x03 \x01(\x08\x12\x19\n\x11pick_min_class_id\x18\x04 \x01(\x08\x12\x1b\n\x13\x62\x61\x63kground_class_id\x18\x05 \x01(\x05\x12\x11\n\tcell_size\x18\x06 \x01(\x05\x12\x1a\n\x0binfer_cells\x18\x07 \x01(\x08:\x05\x66\x61lse\x1a\x80\x01\n SemanticSegmentationRasterSource\x12-\n\x06source\x18\x01 \x02(\x0b\x32\x1d.rv.protos.RasterSourceConfig\x12-\n\x0frgb_class_items\x18\x02 \x03(\x0b\x32\x14.rv.protos.ClassItemB\x15\n\x13label_source_config')
  ,
  dependencies=[rastervision_dot_protos_dot_raster__source__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,rastervision_dot_protos_dot_class__item__pb2.DESCRIPTOR,rastervision_dot_protos_dot_vector__source__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LABELSOURCECONFIG_OBJECTDETECTIONLABELSOURCE = _descriptor.Descriptor(
  name='ObjectDetectionLabelSource',
  full_name='rv.protos.LabelSourceConfig.ObjectDetectionLabelSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_source', full_name='rv.protos.LabelSourceConfig.ObjectDetectionLabelSource.vector_source', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=690,
)

_LABELSOURCECONFIG_CHIPCLASSIFICATIONLABELSOURCE = _descriptor.Descriptor(
  name='ChipClassificationLabelSource',
  full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vector_source', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.vector_source', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ioa_thresh', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.ioa_thresh', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_intersection_over_cell', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.use_intersection_over_cell', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pick_min_class_id', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.pick_min_class_id', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='background_class_id', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.background_class_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cell_size', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.cell_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infer_cells', full_name='rv.protos.LabelSourceConfig.ChipClassificationLabelSource.infer_cells', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=693,
  serialized_end=937,
)

_LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE = _descriptor.Descriptor(
  name='SemanticSegmentationRasterSource',
  full_name='rv.protos.LabelSourceConfig.SemanticSegmentationRasterSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='rv.protos.LabelSourceConfig.SemanticSegmentationRasterSource.source', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rgb_class_items', full_name='rv.protos.LabelSourceConfig.SemanticSegmentationRasterSource.rgb_class_items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=940,
  serialized_end=1068,
)

_LABELSOURCECONFIG = _descriptor.Descriptor(
  name='LabelSourceConfig',
  full_name='rv.protos.LabelSourceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_type', full_name='rv.protos.LabelSourceConfig.source_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_detection_label_source', full_name='rv.protos.LabelSourceConfig.object_detection_label_source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_classification_label_source', full_name='rv.protos.LabelSourceConfig.chip_classification_label_source', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='semantic_segmentation_raster_source', full_name='rv.protos.LabelSourceConfig.semantic_segmentation_raster_source', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.LabelSourceConfig.custom_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_LABELSOURCECONFIG_OBJECTDETECTIONLABELSOURCE, _LABELSOURCECONFIG_CHIPCLASSIFICATIONLABELSOURCE, _LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='label_source_config', full_name='rv.protos.LabelSourceConfig.label_source_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=204,
  serialized_end=1091,
)

_LABELSOURCECONFIG_OBJECTDETECTIONLABELSOURCE.fields_by_name['vector_source'].message_type = rastervision_dot_protos_dot_vector__source__pb2._VECTORSOURCECONFIG
_LABELSOURCECONFIG_OBJECTDETECTIONLABELSOURCE.containing_type = _LABELSOURCECONFIG
_LABELSOURCECONFIG_CHIPCLASSIFICATIONLABELSOURCE.fields_by_name['vector_source'].message_type = rastervision_dot_protos_dot_vector__source__pb2._VECTORSOURCECONFIG
_LABELSOURCECONFIG_CHIPCLASSIFICATIONLABELSOURCE.containing_type = _LABELSOURCECONFIG
_LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE.fields_by_name['source'].message_type = rastervision_dot_protos_dot_raster__source__pb2._RASTERSOURCECONFIG
_LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE.fields_by_name['rgb_class_items'].message_type = rastervision_dot_protos_dot_class__item__pb2._CLASSITEM
_LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE.containing_type = _LABELSOURCECONFIG
_LABELSOURCECONFIG.fields_by_name['object_detection_label_source'].message_type = _LABELSOURCECONFIG_OBJECTDETECTIONLABELSOURCE
_LABELSOURCECONFIG.fields_by_name['chip_classification_label_source'].message_type = _LABELSOURCECONFIG_CHIPCLASSIFICATIONLABELSOURCE
_LABELSOURCECONFIG.fields_by_name['semantic_segmentation_raster_source'].message_type = _LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE
_LABELSOURCECONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_LABELSOURCECONFIG.oneofs_by_name['label_source_config'].fields.append(
  _LABELSOURCECONFIG.fields_by_name['object_detection_label_source'])
_LABELSOURCECONFIG.fields_by_name['object_detection_label_source'].containing_oneof = _LABELSOURCECONFIG.oneofs_by_name['label_source_config']
_LABELSOURCECONFIG.oneofs_by_name['label_source_config'].fields.append(
  _LABELSOURCECONFIG.fields_by_name['chip_classification_label_source'])
_LABELSOURCECONFIG.fields_by_name['chip_classification_label_source'].containing_oneof = _LABELSOURCECONFIG.oneofs_by_name['label_source_config']
_LABELSOURCECONFIG.oneofs_by_name['label_source_config'].fields.append(
  _LABELSOURCECONFIG.fields_by_name['semantic_segmentation_raster_source'])
_LABELSOURCECONFIG.fields_by_name['semantic_segmentation_raster_source'].containing_oneof = _LABELSOURCECONFIG.oneofs_by_name['label_source_config']
_LABELSOURCECONFIG.oneofs_by_name['label_source_config'].fields.append(
  _LABELSOURCECONFIG.fields_by_name['custom_config'])
_LABELSOURCECONFIG.fields_by_name['custom_config'].containing_oneof = _LABELSOURCECONFIG.oneofs_by_name['label_source_config']
DESCRIPTOR.message_types_by_name['LabelSourceConfig'] = _LABELSOURCECONFIG

LabelSourceConfig = _reflection.GeneratedProtocolMessageType('LabelSourceConfig', (_message.Message,), dict(

  ObjectDetectionLabelSource = _reflection.GeneratedProtocolMessageType('ObjectDetectionLabelSource', (_message.Message,), dict(
    DESCRIPTOR = _LABELSOURCECONFIG_OBJECTDETECTIONLABELSOURCE,
    __module__ = 'rastervision.protos.label_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.LabelSourceConfig.ObjectDetectionLabelSource)
    ))
  ,

  ChipClassificationLabelSource = _reflection.GeneratedProtocolMessageType('ChipClassificationLabelSource', (_message.Message,), dict(
    DESCRIPTOR = _LABELSOURCECONFIG_CHIPCLASSIFICATIONLABELSOURCE,
    __module__ = 'rastervision.protos.label_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.LabelSourceConfig.ChipClassificationLabelSource)
    ))
  ,

  SemanticSegmentationRasterSource = _reflection.GeneratedProtocolMessageType('SemanticSegmentationRasterSource', (_message.Message,), dict(
    DESCRIPTOR = _LABELSOURCECONFIG_SEMANTICSEGMENTATIONRASTERSOURCE,
    __module__ = 'rastervision.protos.label_source_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.LabelSourceConfig.SemanticSegmentationRasterSource)
    ))
  ,
  DESCRIPTOR = _LABELSOURCECONFIG,
  __module__ = 'rastervision.protos.label_source_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.LabelSourceConfig)
  ))
_sym_db.RegisterMessage(LabelSourceConfig)
_sym_db.RegisterMessage(LabelSourceConfig.ObjectDetectionLabelSource)
_sym_db.RegisterMessage(LabelSourceConfig.ChipClassificationLabelSource)
_sym_db.RegisterMessage(LabelSourceConfig.SemanticSegmentationRasterSource)


# @@protoc_insertion_point(module_scope)
