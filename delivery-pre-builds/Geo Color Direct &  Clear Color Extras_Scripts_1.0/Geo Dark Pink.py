"""
Geo Color Tools - Scripts Package v2.0
Thanks for download - for commercial and personal uses.
The Geo Color Tools v2.0 granted shall not be copied, distributed, or-sold, offered for resale, transferred in whole or in part except that you may make one copy for archive purposes only.

be.net/dyne
Writen by: Carlos Dordelly
Special thanks: Pancho Contreras, Terry Williams & Roberto Gonzalez

Now you can easily add a quickly reference colors to your objects without lost your applied materials (from any render engine).
Date: 22/07/2017
Written and tested in Cinema 4D R18 / R17 / R16 - Not tested in older versions.

"""

import c4d
from c4d import gui

#color id to apply
gcolor = c4d.Vector(0.4,0.3,0.5) #dark pink

def geo_color():
    
    #get Active Objects
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not activeObjects:
        gui.MessageDialog('Please select one or more objects.')
        return
    
    #start undo action
    doc.StartUndo()

    #geo color actions
    for obj in activeObjects:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE,obj)
        #shorcuts to random functions
        bc = c4d.BaseContainer()
        if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
            if  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT: 
                obj[c4d.ID_BASEOBJECT_USECOLOR]=2
                obj[c4d.ID_BASEOBJECT_COLOR]=gcolor
                tag = obj.MakeTag(c4d.Tdisplay)
                doc.AddUndo(c4d.UNDOTYPE_CHANGE,tag)
                tag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE]=True
                tag[c4d.DISPLAYTAG_SDISPLAYMODE]=6
                tag[c4d.DISPLAYTAG_WDISPLAYMODE]=1
                tag[c4d.ID_BASELIST_NAME]="Geo Wire Color"
                 
            elif  bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT: 
                obj[c4d.ID_BASEOBJECT_USECOLOR]=2
                obj[c4d.ID_BASEOBJECT_COLOR]=gcolor
                obj[c4d.ID_BASEOBJECT_XRAY]=True
                obj.KillTag(c4d.Tdisplay)

            else:
                #obj actions
                obj[c4d.ID_BASEOBJECT_USECOLOR]=2
                obj[c4d.ID_BASEOBJECT_COLOR]=gcolor
                obj[c4d.ID_BASEOBJECT_XRAY]=False
                obj.KillTag(c4d.Tdisplay)

    #end undo action
    doc.EndUndo()

    #do redo action
    doc.DoRedo()

    #update scene
    c4d.EventAdd()
   
 
if __name__=='__main__':
    geo_color()