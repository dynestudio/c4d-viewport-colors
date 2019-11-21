import c4d, os
from c4d import bitmaps, plugins

PLUGIN_ID = 1039371

class Add_geo_color(c4d.plugins.CommandData):
	def geo_color(self, doc):
	    #GetActiveObjects
	    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
	    #Color Dialog
	    cdlg = c4d.gui.ColorDialog(1)
	    #geo color actions
	    for obj in activeObjects:
	        obj[c4d.ID_BASEOBJECT_USECOLOR]=2
	        obj[c4d.ID_BASEOBJECT_COLOR]=cdlg
	    #update scene
	    c4d.EventAdd()
	    return True

	def Execute(self, doc):
		return self.geo_color(doc)

if __name__ == '__main__':
    bmp = bitmaps.BaseBitmap()
    dir, file = os.path.split(__file__)
    fn = os.path.join(dir, "res", "Icon.tif")
    bmp.InitWith(fn)
    result = plugins.RegisterCommandPlugin(PLUGIN_ID, "Geo Color", 0, bmp, "Changes the geometry color", Add_geo_color())