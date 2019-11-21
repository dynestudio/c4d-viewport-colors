import c4d
from c4d import gui

def geo_color():
    
    doc = c4d.documents.GetActiveDocument()
    
    #Get Active Objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    #Color Dialog
    cdlg = c4d.gui.ColorDialog(1)
    
    doc.StartUndo()

    #geo color actions
    for obj in activeObjects:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)
        obj[c4d.ID_BASEOBJECT_USECOLOR]=2
        obj[c4d.ID_BASEOBJECT_COLOR]=cdlg
        tag = obj.MakeTag(c4d.Tdisplay)
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,tag)
        tag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE]=True
        tag[c4d.DISPLAYTAG_SDISPLAYMODE]=6
        tag[c4d.DISPLAYTAG_WDISPLAYMODE]=1
        tag[c4d.ID_BASELIST_NAME]="Display_Geo Wire Color"

    doc.EndUndo()

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()