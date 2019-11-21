import c4d
from c4d import gui

def geo_color():
    doc = c4d.documents.GetActiveDocument()
    #activeObject = doc.GetActiveObject()
    activeObject = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    
    #List of selected objects
    print activeObject
    
    #geo color actions
    activeObject[c4d.ID_BASEOBJECT_USECOLOR]=2
    #cdlg = c4d.gui.ColorDialog(1)
    #activeObject[c4d.ID_BASEOBJECT_COLOR]=cdlg

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()