import c4d
from c4d import gui

def geo_color():
    
    doc = c4d.documents.GetActiveDocument()
    
    #Get Active Objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects: return
    
    #Color Dialog
    cdlg = c4d.gui.ColorDialog(1)
    
    #geo color actions
    for obj in activeObjects:
        obj[c4d.ID_BASEOBJECT_USECOLOR]=2
        obj[c4d.ID_BASEOBJECT_COLOR]=cdlg

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()