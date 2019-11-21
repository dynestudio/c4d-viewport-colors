"""
Viewport Colors - Scripts Package v1.0
Thanks for download - for commercial and personal uses.
The Viewport Colors v1.0 granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Now you can easily add a quickly reference colors to your objects without lost your applied materials (from any render engine).
Date: 29/07/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Not tested in older versions.

"""

import c4d
from c4d import gui

def vp_color():

    #get active objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    #start undo action
    doc.StartUndo()

    #viewport color actions
    for obj in activeObjects:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)
        obj[c4d.ID_BASEOBJECT_COLOR]=c4d.Vector(1,1,1) #set to default
        obj[c4d.ID_BASEOBJECT_USECOLOR]=0 #set to default
        obj[c4d.ID_BASEOBJECT_XRAY]=False #set to default
        obj.KillTag(c4d.Tdisplay) #delete display tag

    #end undo action
    doc.EndUndo()

    #do redo action
    doc.DoRedo() 
    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    vp_color()