import c4d
from c4d import gui

def geo_color():
    
    doc = c4d.documents.GetActiveDocument()
    taglist = doc.GetActiveTags()
    tagname = "Display_Geo Wire Color"

    #Get Active Objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    doc.StartUndo()

    #geo color actions
    for obj in activeObjects:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)
        obj[c4d.ID_BASEOBJECT_USECOLOR]=0
        obj[c4d.ID_BASEOBJECT_XRAY]=False
        delete_tag = obj.KillTag(c4d.Tdisplay)


#    for tag in taglist:
#        if tag[c4d.ID_BASELIST_NAME]=("Display_Geo Wire Color"):
#            tag.Remove()

#    for tag in taglist:
#        if tagname ! = tag.GetType() == c4d.Tdisplay:
#            tag.Remove()

    #tag = op.GetTag(c4d.Tdisplay)
    #print tag
    #if tag[c4d.ID_BASELIST_NAME] == "Display_Geo Wire Color":
        #tag.Remove()
    #c4d.EventAdd()

    doc.EndUndo()
    
    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()