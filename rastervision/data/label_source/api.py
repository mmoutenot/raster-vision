# flake8: noqa

# Registry Keys
LABEL_SOURCE = 'LABEL_SOURCE'

# Deprecated keys provided for backward compatibility.
OBJECT_DETECTION_GEOJSON = 'OBJECT_DETECTION_GEOJSON'
CHIP_CLASSIFICATION_GEOJSON = 'CHIP_CLASSIFICATION_GEOJSON'
SEMANTIC_SEGMENTATION_RASTER = 'SEMANTIC_SEGMENTATION_RASTER'

# OBJECT_DETECTION, CHIP_CLASSIFICATION, SEMANTIC_SEGMENTATION are the keys to use
# and they are already defined in rastervision.task.api

from rastervision.data.label_source.label_source_config import LabelSourceConfig
