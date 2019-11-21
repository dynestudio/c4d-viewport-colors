import c4d
from c4d import gui

def geo_color():
    
    #get active document
    doc = c4d.documents.GetActiveDocument()

    #get active objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    #start undo action
    doc.StartUndo()

    #geo color actions
    for obj in activeObjects:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)
        obj[c4d.ID_BASEOBJECT_COLOR]=c4d.Vector(1,1,1) #set to default
        obj[c4d.ID_BASEOBJECT_USECOLOR]=0 #set to default
        obj[c4d.ID_BASEOBJECT_XRAY]=False #set to default
        obj.KillTag(c4d.Tdisplay) #delete tag

    #end undo action
    doc.EndUndo()
    
    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()