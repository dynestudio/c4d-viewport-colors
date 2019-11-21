import c4d
from c4d import gui

def geo_color():
    
    doc = c4d.documents.GetActiveDocument()
    
    #activeObject = doc.GetActiveObject()
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    
    #geo color actions
    for obj in activeObjects:
        obj[c4d.ID_BASEOBJECT_USECOLOR]=0

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()