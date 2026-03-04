"""QGIS Unit tests for QgsVectorLayerProperties.


.. note:: This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

__author__ = "Benjamin Jakimow"
__date__ = "04/03/2026"
__copyright__ = "Copyright 2026, The QGIS Project"

from qgis.core import QgsVectorLayer, QgsMapLayerType
from qgis.gui import QgsVectorLayerProperties
from qgis.testing import start_app, QgisTestCase

start_app()


class TestQgsVectorLayer(QgisTestCase):

    def test_connect_toggle_editing(self):
        uri = 'Point?crs=epsg:4326&field=id:integer'
        layer = lyr = QgsVectorLayer(uri, 'dummy', 'memory')

        def onToggleEditing(map_layer):
            self.assertEqual(map_layer, layer)

        properties = QgsVectorLayerProperties(None, None, lyr=layer)
        properties.toggleEditing[QgsMapLayerType].connect(onToggleEditing)
        properties.toggleEditing()
