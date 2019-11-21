import c4d
from c4d import gui

def geo_color():
    
    #get active document
    doc = c4d.documents.GetActiveDocument()
    
    #get Active Objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    #color dialog
    cdlg = c4d.gui.ColorDialog(1)
    
    #start undo action
    doc.StartUndo()

    #geo color actions
    for obj in activeObjects:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)
        obj[c4d.ID_BASEOBJECT_USECOLOR]=2
        obj[c4d.ID_BASEOBJECT_COLOR]=cdlg
        obj[c4d.ID_BASEOBJECT_XRAY]=False
        delete_tag=obj.KillTag(c4d.Tdisplay)

    doc.EndUndo()

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()