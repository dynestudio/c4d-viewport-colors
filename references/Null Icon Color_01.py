import c4d
from c4d import gui

NULL_ID = 5140

def null_i_color():
    
    #get Active Objects
    activeObject = doc.GetActiveObject()
    typeObject = activeObject.GetType()

    if not activeObject:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    if not typeObject == NULL_ID:
        gui.MessageDialog('Please select one null.')
        return

    #color dialog
    cdlg = c4d.gui.ColorDialog(1)
    if cdlg == None:
        gui.MessageDialog('No color selected.')
        return
    
    #start undo action
    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_CHANGE,activeObject)
    
    #ops
    activeObject[c4d.ID_BASEOBJECT_USECOLOR]=2
    activeObject[c4d.ID_BASEOBJECT_COLOR]=cdlg
    activeObject[c4d.NULLOBJECT_ICONCOL]=True

    #end undo action
    doc.EndUndo()

    #do redo action
    doc.DoRedo()

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    null_i_color()