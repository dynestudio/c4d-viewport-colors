import c4d
from c4d import gui

def geo_color():
    doc = c4d.documents.GetActiveDocument()

    activeObject = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    #activeObject[c4d.ID_BASEOBJECT_USECOLOR]=2
    #cdlg = c4d.gui.ColorDialog(1)
    #activeObject[c4d.ID_BASEOBJECT_COLOR]=cdlg

    c4d.EventAdd()
    print activeObject

if __name__=='__main__':
    geo_color()



 -------------------------------------------

 import c4d

def getchildren_v1(op, stop_obj, data=None):
    if not data:
        data = list()
        
    while op:
        data.append(op)
        getchildren_v1(op.GetDown(), stop_obj, data)
        op = op.GetNext()
        if op == stop_obj:
            return data
        
def getchildren_v2(op, data=None):
    if not data:
        data = list()
        
    data.append(op)
    children = op.GetChildren()
    for child in children:
        getchildren_v2(child, data)
        
    return data
    

def main():
    obj = doc.GetActiveObject()
    my_list_v1 = getchildren_v1(obj, obj.GetNext())
    print my_list_v1
    
    my_list_v2 = getchildren_v2(obj)
    print my_list_v2
    getchildren_v1(obj, obj.GetNext())[c4d.ID_BASEOBJECT_USECOLOR]=2

if __name__=='__main__':
    main()

  -----------------------------------------