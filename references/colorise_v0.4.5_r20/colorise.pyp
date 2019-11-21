# Colorise v0.4.5 R20
# By aturtur

# Libraries
import c4d, maxon, os
import random as rnd
from c4d import storage as s
from c4d import gui, plugins, bitmaps, documents
from c4d.modules import colorchooser
try:
    import redshift
except:
    pass

# Testing ids 1000001 - 1000010
# be sure to use a unique ID obtained from www.plugincafe.com
#----------------------------------------------------------------------------------------------------
PLUGIN_ID = 1041363
    
BUTTON_A = 11020
BUTTON_B = 11021
BUTTON_C = 11022
BUTTON_D = 11023
BUTTON_E = 11024
BUTTON_F = 11025
BUTTON_G = 11026
BUTTON_H = 11027

BUTTON_I = 11028
BUTTON_J = 11029
BUTTON_K = 11030
BUTTON_L = 11031
BUTTON_M = 11032
BUTTON_N = 11033
BUTTON_O = 11034
BUTTON_P = 11035

BUTTON_RESET = 11038
BUTTON_DEFAULT = 11039

COLOR_A  = 11000
COLOR_B  = 11001
COLOR_C  = 11002
COLOR_D  = 11003
COLOR_E  = 11004
COLOR_F  = 11005
COLOR_G  = 11006
COLOR_H  = 11007

COLOR_I  = 11008
COLOR_J  = 11009
COLOR_K  = 11010
COLOR_L  = 11011
COLOR_M  = 11012
COLOR_N  = 11013
COLOR_O  = 11014
COLOR_P  = 11015

MENU_LOAD = 11050
MENU_SAVE = 11051
MENU_RESET = 11052
MENU_SET = 11053
MENU_ABLACK = 11054
MENU_CRTMAT = 11056
MENU_LDSW = 11057
MENU_CRTSW = 11058

#----------------------------------------------------------------------------------------------------
colorsDict = {
    11020: 11000,
    11021: 11001,
    11022: 11002,
    11023: 11003,
    11024: 11004,
    11025: 11005,
    11026: 11006,
    11027: 11007,
    11028: 11008,
    11029: 11009,
    11030: 11010,
    11031: 11011,
    11032: 11012,
    11033: 11013,
    11034: 11014,
    11035: 11015,
}

presetsDict = {}

objectList = [
    "BaseObject",
    "PolygonObject",
    "SplineObject",
    "HairObject",
    "VoronoiFracture",
    "CameraObject", "LodObject",
    "MotionTrackerObject",
    "CAJointObject"
]

rsNodes = {
    "Output": c4d.Vector(0.286, 0.329, 0.463),
    "RS Architectural": c4d.Vector(0.529, 0.345, 0.333),
    "RS Matte-Shadow Catcher": c4d.Vector(0.529, 0.345, 0.333),
    "RS Car Paint": c4d.Vector(0.529, 0.345, 0.333),
    "RS Hair": c4d.Vector(0.529, 0.345, 0.333),
    "RS Incandescent": c4d.Vector(0.529, 0.345, 0.333),
    "RS Material": c4d.Vector(0.529, 0.345, 0.333),
    "RS Material Blender": c4d.Vector(0.529, 0.345, 0.333),
    "RS Skin": c4d.Vector(0.529, 0.345, 0.333),
    "RS Sprite": c4d.Vector(0.529, 0.345, 0.333),
    "RS SSS": c4d.Vector(0.529, 0.345, 0.333),
    "RS Normal Map": c4d.Vector(0.663, 0.624, 0.424),
    "RS AO": c4d.Vector(0.663, 0.624, 0.424),
    "RS Camera Map": c4d.Vector(0.663, 0.624, 0.424),
    "RS Curvature": c4d.Vector(0.663, 0.624, 0.424),
    "RS Noise": c4d.Vector(0.663, 0.624, 0.424),
    "RS Ramp": c4d.Vector(0.663, 0.624, 0.424),
    "RS Texture": c4d.Vector(0.663, 0.624, 0.424),
    "WireFrame": c4d.Vector(0.663, 0.624, 0.424),
    "RS Store Color To AOV": c4d.Vector(0.69, 0.663, 0.78),
    "RS Store Integer To AOV": c4d.Vector(0.69, 0.663, 0.78),
    "RS Store Scalar To AOV": c4d.Vector(0.69, 0.663, 0.78),
    "RS Point Attribute": c4d.Vector(0.345, 0.31, 0.459),
    "RS Vertex Attribute": c4d.Vector(0.345, 0.31, 0.459),
    "RS Bump Blender": c4d.Vector(0.345, 0.31, 0.459),
    "RS Bump Map": c4d.Vector(0.345, 0.31, 0.459),
    "C4D Shader": c4d.Vector(0.424, 0.392, 0.541),
    "RS Displacement": c4d.Vector(0.345, 0.31, 0.459),
    "RS Displacement Blender": c4d.Vector(0.345, 0.31, 0.459),
    "RS C4D Hair Attributes": c4d.Vector(0.533, 0.502, 0.639),
    "RS Hair Position": c4d.Vector(0.533, 0.502, 0.639),
    "RS Hair Random Color": c4d.Vector(0.533, 0.502, 0.639),
    "RS Ray Switch": c4d.Vector(0.533, 0.502, 0.639),
    "RS Shader Switch": c4d.Vector(0.533, 0.502, 0.639),
    "RS Color User Data": c4d.Vector(0.69, 0.663, 0.78),
    "RS Integer User Data": c4d.Vector(0.69, 0.663, 0.78),
    "RS Scalar User Data": c4d.Vector(0.69, 0.663, 0.78),
    "RS Vector User Data": c4d.Vector(0.69, 0.663, 0.78),
    "RS Fresnel": c4d.Vector(0.424, 0.392, 0.541),
    "Remark": c4d.Vector(0.369, 0.431, 0.49),
    "RS Round Corners": c4d.Vector(0.424, 0.392, 0.541),
    "RS State": c4d.Vector(0.424, 0.392, 0.541),
    "RS TriPlanar": c4d.Vector(0.424, 0.392, 0.541),
    "RS Environment": c4d.Vector(0.761, 0.694, 0.784),
    "RS Physical Sky": c4d.Vector(0.761, 0.694, 0.784),
    "RS Dome Light": c4d.Vector(0.91, 0.8, 0.529),
    "RS IES Light": c4d.Vector(0.91, 0.8, 0.529),
    "RS Physical Light": c4d.Vector(0.91, 0.8, 0.529),
    "RS Portal Light": c4d.Vector(0.91, 0.8, 0.529),
    "RS Sun Light": c4d.Vector(0.91, 0.8, 0.529),
    "RS Volume": c4d.Vector(0.529, 0.494, 0.333),
    "RS Abs": c4d.Vector(0.537, 0.71, 0.569),
    "RS Add": c4d.Vector(0.537, 0.71, 0.569),
    "RS Arccosine": c4d.Vector(0.537, 0.71, 0.569),
    "RS Arcsine": c4d.Vector(0.537, 0.71, 0.569),
    "RS ArcTan2": c4d.Vector(0.537, 0.71, 0.569),
    "RS Arctangent": c4d.Vector(0.537, 0.71, 0.569),
    "RS Bias": c4d.Vector(0.537, 0.71, 0.569),
    "RS Change Range": c4d.Vector(0.537, 0.71, 0.569),
    "RS Cosine": c4d.Vector(0.537, 0.71, 0.569),
    "RS Cross Product": c4d.Vector(0.537, 0.71, 0.569),
    "RS Div": c4d.Vector(0.537, 0.71, 0.569),
    "RS Dot Product": c4d.Vector(0.537, 0.71, 0.569),
    "RS Exp": c4d.Vector(0.537, 0.71, 0.569),
    "RS Floor": c4d.Vector(0.537, 0.71, 0.569),
    "RS Frac": c4d.Vector(0.537, 0.71, 0.569),
    "RS Gain": c4d.Vector(0.537, 0.71, 0.569),
    "RS Invert": c4d.Vector(0.537, 0.71, 0.569),
    "RS Ln": c4d.Vector(0.537, 0.71, 0.569),
    "RS Log": c4d.Vector(0.537, 0.71, 0.569),
    "RS Max": c4d.Vector(0.537, 0.71, 0.569),
    "RS Min": c4d.Vector(0.537, 0.71, 0.569),
    "RS Mix": c4d.Vector(0.537, 0.71, 0.569),
    "RS Mod": c4d.Vector(0.537, 0.71, 0.569),
    "RS Mul": c4d.Vector(0.537, 0.71, 0.569),
    "RS Neg": c4d.Vector(0.537, 0.71, 0.569),
    "RS Normalize": c4d.Vector(0.537, 0.71, 0.569),
    "RS Pow": c4d.Vector(0.537, 0.71, 0.569),
    "RS Rcp": c4d.Vector(0.537, 0.71, 0.569),
    "RS Saturate": c4d.Vector(0.537, 0.71, 0.569),
    "RS Sign": c4d.Vector(0.537, 0.71, 0.569),
    "RS Sine": c4d.Vector(0.537, 0.71, 0.569),
    "RS Sqrt": c4d.Vector(0.537, 0.71, 0.569),
    "RS Sub": c4d.Vector(0.537, 0.71, 0.569),
    "RS Tangent": c4d.Vector(0.537, 0.71, 0.569),
    "RS Vector Abs": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Add": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Bias": c4d.Vector(0,0,0),
    "RS Vector Change Range": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Div": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Exp": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Floor": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Frac": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Gain": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Invert": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Length": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Ln": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Log": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Max": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Min": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Mix": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Mod": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Mul": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Neg": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Pow": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Rcp": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Saturate": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Sign": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Sqrt": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector Sub": c4d.Vector(0.325, 0.51, 0.357),
    "RS Vector To Scalars": c4d.Vector(0.325, 0.51, 0.357),
    "Constant": c4d.Vector(0.537, 0.71, 0.569),
    "RS Color Abs": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Change Range": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Composite": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Correct": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Exp": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Gain": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Invert": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Layer": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Maker": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Mix": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Saturate": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Splitter": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color Sub": c4d.Vector(0.788, 0.557, 0.537),
    "RS Color To HSV": c4d.Vector(0.788, 0.557, 0.537),
    "RS HSV To Color": c4d.Vector(0.788, 0.557, 0.537),
    "RS Vector Bias": c4d.Vector(0,0,0)
}
#----------------------------------------------------------------------------------------------------
# [ Functions ]

# Identify objet
def IdentifyObject(obj):
    className = type(obj).__name__
    TypeName = obj.GetTypeName()
    if className == "XPressoTag":
        return "Xpresso"
    elif className == "BaseTag":
        return "Tag"
    elif className == "BaseObject":
        if TypeName == "Null":
            return "Null"
        return "Object"
    elif className == "PolygonObject":
        return "Object"
    elif className == "SplineObject":
        return "Object"
    elif className == "HairObject":
        return "Object"
    elif className == "VoronoiFracture":
        return "Object"
    elif className == "CameraObject":
        return "Object"
    elif className == "LodObject":
        return "Object"
    elif className == "MotionTrackerObject":
        return "Object"
    elif className == "CAJointObject":
        return "CAJointObject"
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# Change color
def ChangeColor(color):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    #------------------------------------- 
    xpressoFound = False
    #------------------------------------- 
    selection = doc.GetSelection()
    #------------------------------------- Xpresso
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            xpressoFound = True
    #-------------------------------------
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            nm = s.GetNodeMaster()
            root = nm.GetRoot()
            for c in root.GetChildren():
                if c.GetBit(c4d.BIT_ACTIVE):
                    nm.AddUndo()
                    c[c4d.ID_GVBASE_COLOR] = color
        elif IdentifyObject(s) == "CAJointObject" and xpressoFound == False:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                    s[c4d.ID_BASEOBJECT_USECOLOR] = 2
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                    s[c4d.ID_BASEOBJECT_COLOR] = color
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                    s[c4d.ID_CA_JOINT_OBJECT_ICONCOL] = 1
        elif IdentifyObject(s) == "Null" and xpressoFound == False:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_USECOLOR] = 2
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_COLOR] = color
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.NULLOBJECT_ICONCOL] = 1
        elif type(s).__name__ in objectList and xpressoFound == False:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_USECOLOR] = 2
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_COLOR] = color

    doc.EndUndo()
    c4d.EventAdd()

def RedshiftChangeColor(color):                 # Redshift
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    materials = doc.GetMaterials()
    try:
        for m in materials:
            if m.GetBit(c4d.BIT_ACTIVE):
                rsnm = redshift.GetRSMaterialNodeMaster(m)
                rsroot = rsnm.GetRoot()
                for c in rsroot.GetChildren():
                    if c.GetBit(c4d.BIT_ACTIVE):
                        rsnm.AddUndo()
                        c[c4d.ID_GVBASE_COLOR] = color
    except:
        pass
    doc.EndUndo()
    c4d.EventAdd()
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 
# Default color
def DefaultColor():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()    
    selection = doc.GetSelection()
    #-------------------------------------
    xpressoFound = False
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            xpressoFound = True
    #-------------------------------------
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            nm = s.GetNodeMaster()
            root = nm.GetRoot()
            for c in root.GetChildren():
                if c.GetBit(c4d.BIT_ACTIVE):
                    nm.AddUndo()
                    c[c4d.ID_GVBASE_COLOR] = c4d.Vector(97.0/255.0,98.0/255.0,100.0/255.0)
        elif IdentifyObject(s) == "CAJointObject" and xpressoFound == False:
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                    s[c4d.ID_BASEOBJECT_USECOLOR] = 1
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                    s[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(0.8, 0.839, 0.878)
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                    s[c4d.ID_CA_JOINT_OBJECT_ICONCOL] = 0
        elif IdentifyObject(s) == "Null" and xpressoFound == False:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_USECOLOR] = 0
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(90.0/255.0,97.0/255.0,105.0/255.0)
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.NULLOBJECT_ICONCOL] = 0
        elif type(s).__name__ in objectList and xpressoFound == False:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_USECOLOR] = 0
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_COLOR] = c4d.Vector(90.0/255.0,97.0/255.0,105.0/255.0)
    doc.EndUndo()
    c4d.EventAdd()
#....................................................................................................
# Assign to layer
def AssignLayer(obj, color):
    doc = c4d.documents.GetActiveDocument()
    allLayers = CollectLayers()
    for layer in allLayers:
        if layer[c4d.ID_LAYER_COLOR] == color:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
            obj.SetLayerObject(layer)

# Remove layer
def RemoveLayer():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    selection = doc.GetSelection()
    for s in selection:
        if IdentifyObject(s) == "Object" or IdentifyObject(s) == "Null" or IdentifyObject(s) == "CAJointObject":
            s.SetLayerObject(None)
    c4d.EventAdd()
            
# Create layer
def CreateLayer(color):
    doc = c4d.documents.GetActiveDocument()
    layerRoot = doc.GetLayerObjectRoot()
    layer = c4d.documents.LayerObject()
    layer.SetName("Layer")
    layer[c4d.ID_LAYER_COLOR] = color
    layer.InsertUnder(layerRoot)
    doc.AddUndo(c4d.UNDOTYPE_NEW, layer)

#...........................................
# Get next object
def GetNextObject(op):
    if op==None:
        return None
    if op.GetDown():
        return op.GetDown()
    while not op.GetNext() and op.GetUp():
        op = op.GetUp()
    return op.GetNext() 

# Iterate
def IterateHierarchy(op):
    layerList = []
    if op is None:
        return
    while op:
        layerList.append(op)
        op = GetNextObject(op)
    return layerList

# Collect layers
def CollectLayers():
    doc = c4d.documents.GetActiveDocument()
    layerRoot = doc.GetLayerObjectRoot()
    layers = layerRoot.GetChildren()
    if layers == []:
        return None
    else:
        startLayer = layers[0]
        return IterateHierarchy(startLayer)


# Check if layer exists (Iterate all layers)
def DeepCheckLayer(color):
    colorExists = False
    allLayers = CollectLayers()
    if allLayers == None:
        return colorExists
    else:    
        for layer in allLayers:
            if layer[c4d.ID_LAYER_COLOR] == color:
                colorExists = True
        return colorExists
#...........................................

# Layer function
def LayerThing(color):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    # Objects
    selection = doc.GetSelection()
    for s in selection:
        if IdentifyObject(s) == "Object" or IdentifyObject(s) == "Null" or IdentifyObject(s) == "CAJointObject":
            if not DeepCheckLayer(color):
                CreateLayer(color)
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                AssignLayer(s, color)
            else:
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
                AssignLayer(s, color)

    doc.EndUndo()
    c4d.EventAdd()
#....................................................................................................
# Redshift support

def RedshiftChangeColor(color):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    materials = doc.GetMaterials()
    try:
        for m in materials:
            if m.GetBit(c4d.BIT_ACTIVE):
                rsnm = redshift.GetRSMaterialNodeMaster(m)
                rsroot = rsnm.GetRoot()
                for c in rsroot.GetChildren():
                    if c.GetBit(c4d.BIT_ACTIVE):
                        rsnm.AddUndo()
                        c[c4d.ID_GVBASE_COLOR] = color
    except:
        pass
    doc.EndUndo()
    c4d.EventAdd()

def RedshiftDefaultColor():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    materials = doc.GetMaterials()
    try:
        for m in materials:
            if m.GetBit(c4d.BIT_ACTIVE):
                rsnm = redshift.GetRSMaterialNodeMaster(m)
                rsroot = rsnm.GetRoot()
                for c in rsroot.GetChildren():
                    if c.GetBit(c4d.BIT_ACTIVE):
                        if c.GetName() in rsNodes:
                            if  c.GetName() == "RS Vector Bias":
                                if c.GetOutPort(0).GetName(c) == "Out":
                                    rsnm.AddUndo()
                                    c[c4d.ID_GVBASE_COLOR] = c4d.Vector(0.325, 0.51, 0.357)
                                else:
                                    rsnm.AddUndo()
                                    c[c4d.ID_GVBASE_COLOR] = c4d.Vector(0.788, 0.557, 0.537)
                            else:
                                rsnm.AddUndo()
                                c[c4d.ID_GVBASE_COLOR] = rsNodes[c.GetName()]
                        else:
                            rsnm.AddUndo()
                            c[c4d.ID_GVBASE_COLOR] = c4d.Vector(97.0/255.0,98.0/255.0,100.0/255.0)
    except:
        pass
    doc.EndUndo()
    c4d.EventAdd()
#....................................................................................................
# Group function
def DeSelect(data):
    doc = c4d.documents.GetActiveDocument()
    dataType = type(data).__name__
    # List
    if dataType == "list":
        lst = data
        for obj in lst:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, obj)
            obj.DelBit(c4d.BIT_ACTIVE)
    # Single object
    elif dataType == "BaseObject":
        obj = data
        doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, obj)
        obj.DelBit(c4d.BIT_ACTIVE)

def SelectChildren(obj,next):
    doc = c4d.documents.GetActiveDocument()
    while obj and obj != next:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, obj)
        obj.SetBit(c4d.BIT_ACTIVE)
        SelectChildren(obj.GetDown(), next)
        obj = obj.GetNext()
    return True

def GroupThing(color):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    c4d.CallCommand(100004772) # Group objects
    null = doc.GetSelection()[0]
    null[c4d.ID_BASEOBJECT_USECOLOR] = 2
    null[c4d.NULLOBJECT_DISPLAY] = 0
    null[c4d.NULLOBJECT_ICONCOL] = 1
    null[c4d.ID_BASEOBJECT_COLOR] = color

    # Select children
    for obj in doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN):
            if SelectChildren(obj, obj.GetNext()):
                obj.DelBit(c4d.BIT_ACTIVE)

    selection = doc.GetSelection()
    for s in selection:
        if IdentifyObject(s) == "Object" or IdentifyObject(s) == "Null" or IdentifyObject(s) == "CAJointObject":
            if not DeepCheckLayer(color):
                CreateLayer(color)
                AssignLayer(s, color)
            else:
                AssignLayer(s, color)
    DeSelect(selection)
    AssignLayer(null, color)
    doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, null)
    null.SetBit(c4d.BIT_ACTIVE)
    doc.EndUndo()
    c4d.EventAdd()
#....................................................................................................
def RandomColor(colors):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    i = 0
    length = len(colors)
    #-------------------------------------
    xpressoFound = False
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            xpressoFound = True
    #-------------------------------------
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            nm = s.GetNodeMaster()
            root = nm.GetRoot()
            for c in root.GetChildren():
                if c.GetBit(c4d.BIT_ACTIVE):
                    nm.AddUndo()
                    c[c4d.ID_GVBASE_COLOR] = colors[i % length]
                    i += 1
        elif IdentifyObject(s) == "Null" and xpressoFound == False:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_USECOLOR] = 2
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_COLOR] = colors[i % length]
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.NULLOBJECT_ICONCOL] = 1
            i += 1
        elif type(s).__name__ in objectList and xpressoFound == False:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_USECOLOR] = 2
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, s)
            s[c4d.ID_BASEOBJECT_COLOR] = colors[i % length]
            i += 1
    doc.EndUndo()
    c4d.EventAdd()
#....................................................................................................
def CreateMaterials(colors):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    for i in range(0, 16):
        mat = c4d.BaseMaterial(c4d.Mmaterial)
        mat[c4d.MATERIAL_USE_REFLECTION] = 0
        mat[c4d.MATERIAL_USE_LUMINANCE] = 0
        mat[c4d.MATERIAL_USE_COLOR] = 1
        mat[c4d.MATERIAL_COLOR_COLOR] = colors[i]
        mat[c4d.MATERIAL_LUMINANCE_COLOR] = colors[i]
        mat.Message(c4d.MSG_UPDATE)
        mat.Update(True, True)
        doc.InsertMaterial(mat)
        doc.AddUndo(c4d.UNDOTYPE_NEW, mat)        
        c4d.EventAdd()
    doc.EndUndo()
    pass
#....................................................................................................
def CreateSwatches(colors):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    csd = colorchooser.ColorSwatchData(doc)
    csg = colorchooser.ColorSwatchGroup("Colorise", False)
    for c in colors:
        color = maxon.ColorA64(c[0], c[1], c[2], 1)    
        csg.AddColor(color, False, -1)
    csd.InsertGroup(csg, -1, c4d.SWATCH_CATEGORY_DOCUMENT)
    csd.Save(doc)
    c4d.EventAdd()
    doc.EndUndo()
    pass
#....................................................................................................
def tool():
    doc = c4d.documents.GetActiveDocument()
    return doc.GetActiveToolData()
#....................................................................................................
def GetNextObjectST(op):
    if op==None:
        return None
    if op.GetDown():
        return op.GetDown()
    while not op.GetNext() and op.GetUp():
        op = op.GetUp()
    return op.GetNext() 
 
def IterateHierarchyST(op, color):
    doc = c4d.documents.GetActiveDocument()
    if op is None:
        return
    while op:
        if op[c4d.ID_BASEOBJECT_COLOR] == color:
            doc.AddUndo(c4d.UNDOTYPE_BITS, op)
            op.SetBit(c4d.BIT_ACTIVE)
        op = GetNextObjectST(op)
    return True

def SelectThing(color, add = 0):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    start_object = doc.GetFirstObject()
    selection = doc.GetSelection()
    #------------------------------------- Redshift
    redshiftFound = False
    materials = doc.GetMaterials()
    try:
        for m in materials:
            if m.GetBit(c4d.BIT_ACTIVE): # Material active
                rsnm = redshift.GetRSMaterialNodeMaster(m)
                rsroot = rsnm.GetRoot()
                redshiftFound = True
    except:
        pass
    #-------------------------------------
    xpressoFound = False
    for s in selection:
        if IdentifyObject(s) == "Xpresso":
            xpressoFound = True
    #-------------------------------------
    if add == 0 and xpressoFound == False:
        for x in selection:
            doc.AddUndo(c4d.UNDOTYPE_BITS, x)
            x.DelBit(c4d.BIT_ACTIVE)
    elif add == 0 and xpressoFound == True:
        for s in selection:
            if IdentifyObject(s) == "Xpresso":
                nm = s.GetNodeMaster()
                root = nm.GetRoot()
                for c in root.GetChildren():
                    c.DelBit(c4d.BIT_ACTIVE)
    if add == 0 and redshiftFound == True: #Redshift
        try:
            for m in materials:
                if m.GetBit(c4d.BIT_ACTIVE): # Material active
                    rsnm = redshift.GetRSMaterialNodeMaster(m)
                    rsroot = rsnm.GetRoot()
                    for c in rsroot.GetChildren():
                        if c.GetBit(c4d.BIT_ACTIVE):
                            rsnm.AddUndo()
                            c.DelBit(c4d.BIT_ACTIVE)
        except:
            pass

    #-------------------------------------
    if xpressoFound == False and redshiftFound == False:
        IterateHierarchyST(start_object, color)
        # Workaround to centerize axis -----------
        c4d.CallCommand(100004772) # Group Objects
        c4d.CallCommand(12105) # Undo
        # ----------------------------------------
    elif xpressoFound == True:
        for s in selection:
            if IdentifyObject(s) == "Xpresso":
                nm = s.GetNodeMaster()
                root = nm.GetRoot()
                for c in root.GetChildren():
                    if c[c4d.ID_GVBASE_COLOR] == color:
                        c.SetBit(c4d.BIT_ACTIVE)
    elif redshiftFound == True:
        try:
            for m in materials:
                if m.GetBit(c4d.BIT_ACTIVE): # Material active
                    rsnm = redshift.GetRSMaterialNodeMaster(m)
                    rsroot = rsnm.GetRoot()
                    for r in rsroot.GetChildren():
                        if r[c4d.ID_GVBASE_COLOR] == color:
                            rsnm.AddUndo()
                            r.SetBit(c4d.BIT_ACTIVE)
        except:
            pass

    c4d.EventAdd()
    doc.EndUndo()
    pass
#----------------------------------------------------------------------------------------------------
def IterateHierarchySL(op, color):
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()
    if op is None:
        return
    while op:
        try:
            if op[c4d.ID_LAYER_LINK][c4d.ID_LAYER_COLOR] == color:
                doc.AddUndo(c4d.UNDOTYPE_BITS, op)
                op.SetBit(c4d.BIT_ACTIVE)
        except:
            pass
        op = GetNextObjectST(op)
    return True

def SelectLayer(color, add):
    doc = c4d.documents.GetActiveDocument()
    start_object = doc.GetFirstObject()
    selection = doc.GetSelection()
    
    if add == 0:
        for x in selection:
            doc.AddUndo(c4d.UNDOTYPE_BITS, x)
            x.DelBit(c4d.BIT_ACTIVE)

    IterateHierarchySL(start_object, color)


    c4d.EventAdd()
    doc.EndUndo()
    pass
#----------------------------------------------------------------------------------------------------
# GUI
class MyDialog(gui.GeDialog):
        
    def CreateLayout(self):

        self.SetTitle("Colorise")
        
        # Menu: File
        self.MenuSubBegin("File")
        self.MenuAddString(11052,"Reset palette")
        self.MenuAddString(11050,"Load from file")
        self.MenuAddString(11051,"Save to file")
        self.MenuAddString(11053,"Set as default")
        self.MenuAddString(11054,"All black")
        self.MenuAddSeparator()        
        self.MenuAddString(11057,"Load from swatches")
        self.MenuAddString(11058,"Create swatches")
        self.MenuAddString(11056,"Create materials")
        self.MenuAddSeparator()
        i = 0
        presetBase = 11100
        path, fn = os.path.split(__file__)
        try:
            for file in os.listdir(path+"/presets"):
                if file.endswith(".txt"):
                    presetPath = os.path.join(path+"/presets", file)
                    presetName = os.path.splitext(file)[0]
                    presetId = presetBase+i
                    self.MenuAddString(presetId, presetName)
                    presetsDict[presetId] = presetPath
                    i = i+1
        except:
            pass
        self.MenuSubEnd()
        self.MenuFinished()
        # -----------------------------------------------------------------------------------
        # GUI
        # Color selectors
        self.GroupBegin(1001, c4d.BFH_LEFT | c4d.BFV_TOP, 1, 17, c4d.BFV_GRIDGROUP_EQUALCOLS)

        # A
        self.GroupBegin(1002, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_A, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_A, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # B
        self.GroupBegin(1003, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_B, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_B, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # C
        self.GroupBegin(1004, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_C, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_C, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # D
        self.GroupBegin(1005, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_D, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_D, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # E
        self.GroupBegin(1006, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_E, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_E, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # F
        self.GroupBegin(1007, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_F, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_F, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # G
        self.GroupBegin(1008, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_G, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_G, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # H
        self.GroupBegin(1009, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_H, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_H, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # I
        self.GroupBegin(1010, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_I, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_I, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # J
        self.GroupBegin(1011, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_J, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_J, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # K
        self.GroupBegin(1012, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_K, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_K, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # L
        self.GroupBegin(1013, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_L, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_L, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # M
        self.GroupBegin(1014, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_M, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_M, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # N
        self.GroupBegin(1015, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_N, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_N, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # O
        self.GroupBegin(1016, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_O, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_O, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # P
        self.GroupBegin(1017, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_P, c4d.BFH_CENTER | c4d.BFV_TOP, initw=14, inith=10, name=" ")
        self.AddColorField(COLOR_P, c4d.BFH_CENTER | c4d.BFV_TOP, 50)
        self.GroupEnd()

        # RESET AND DEFAULT
        self.GroupBegin(1018, c4d.BFH_CENTER | c4d.BFV_TOP, 2, 1, c4d.BFV_GRIDGROUP_EQUALCOLS)
        self.AddButton(BUTTON_DEFAULT, c4d.BFH_CENTER | c4d.BFV_TOP, initw=50, inith=25, name="X")
        self.GroupEnd()
        
        self.GroupEnd()

        #--------------------------------------------------------------------------------------------
        # load template colours from a file
        try:
            path, fn = os.path.split(__file__)
            coloursFile = os.path.join(path, "res", "default.txt")
            coloursArray = []
            f = open(coloursFile.decode("utf-8"))
            for line in f:
                line = line.split(",")
                r = float(line[0])
                g = float(line[1])
                b = float(line[2])
                coloursArray.append(c4d.Vector(r/255.0,g/255.0,b/255.0))
            self.SetColorField(COLOR_A, coloursArray[0], 1, 1, 0)
            self.SetColorField(COLOR_B, coloursArray[1], 1, 1, 0)
            self.SetColorField(COLOR_C, coloursArray[2], 1, 1, 0)
            self.SetColorField(COLOR_D, coloursArray[3], 1, 1, 0)
            self.SetColorField(COLOR_E, coloursArray[4], 1, 1, 0)
            self.SetColorField(COLOR_F, coloursArray[5], 1, 1, 0)
            self.SetColorField(COLOR_G, coloursArray[6], 1, 1, 0)
            self.SetColorField(COLOR_H, coloursArray[7], 1, 1, 0)
            self.SetColorField(COLOR_I, coloursArray[8], 1, 1, 0)
            self.SetColorField(COLOR_J, coloursArray[9], 1, 1, 0)
            self.SetColorField(COLOR_K, coloursArray[10], 1, 1, 0)
            self.SetColorField(COLOR_L, coloursArray[11], 1, 1, 0)
            self.SetColorField(COLOR_M, coloursArray[12], 1, 1, 0)
            self.SetColorField(COLOR_N, coloursArray[13], 1, 1, 0)
            self.SetColorField(COLOR_O, coloursArray[14], 1, 1, 0)
            self.SetColorField(COLOR_P, coloursArray[15], 1, 1, 0)
            f.close()
        except:
            pass

        return True
    #------------------------------------------------------------------------------------------------

    #------------------------------------------------------------------------------------------------
    def Command(self, id, msg):
        doc = c4d.documents.GetActiveDocument()
        bc = c4d.BaseContainer()
        # Button commands
        if (id in colorsDict):
            if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
                color = self.GetColorField(colorsDict[id])["color"]
                if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT:
                    # Shift pressed
                    if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT:
                        # Shift and Alt pressed
                        SelectThing(color, 1)
                        return True
                    LayerThing(color)
                    return True
                elif bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QCTRL:
                    # Control pressed
                    if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT:
                        # Control and Alt pressed
                        if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT:
                        # Control, Alt and Shift pressed
                            SelectLayer(color, 1)
                            return True
                        SelectLayer(color, 0)
                        return True
                    try:
                        GroupThing(color)
                    except:
                        pass
                    return True
                elif bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT:
                    # Alt pressed
                    SelectThing(color, 0)
                    return True
                else:
                    # No input qualifier
                    ChangeColor(color)
                    RedshiftChangeColor(color)

                    try: obj = doc.GetActiveObjects(False)[0]
                    except: tool()[c4d.MDATA_DOODLE_COLOR] = color

                    return True
        #--------------------------------------------------------------------------------------------
        # Reset palette
        if (id == MENU_RESET):
            try:
                path, fn = os.path.split(__file__)
                coloursFile = os.path.join(path, "res", "default.txt")
                coloursArray = []
                f = open(coloursFile.decode("utf-8"))
                for line in f:
                    line = line.split(",")
                    r = float(line[0])
                    g = float(line[1])
                    b = float(line[2])
                    coloursArray.append(c4d.Vector(r/255.0,g/255.0,b/255.0))
                self.SetColorField(COLOR_A, coloursArray[0], 1, 1, 0)
                self.SetColorField(COLOR_B, coloursArray[1], 1, 1, 0)
                self.SetColorField(COLOR_C, coloursArray[2], 1, 1, 0)
                self.SetColorField(COLOR_D, coloursArray[3], 1, 1, 0)
                self.SetColorField(COLOR_E, coloursArray[4], 1, 1, 0)
                self.SetColorField(COLOR_F, coloursArray[5], 1, 1, 0)
                self.SetColorField(COLOR_G, coloursArray[6], 1, 1, 0)
                self.SetColorField(COLOR_H, coloursArray[7], 1, 1, 0)
                self.SetColorField(COLOR_I, coloursArray[8], 1, 1, 0)
                self.SetColorField(COLOR_J, coloursArray[9], 1, 1, 0)
                self.SetColorField(COLOR_K, coloursArray[10], 1, 1, 0)
                self.SetColorField(COLOR_L, coloursArray[11], 1, 1, 0)
                self.SetColorField(COLOR_M, coloursArray[12], 1, 1, 0)
                self.SetColorField(COLOR_N, coloursArray[13], 1, 1, 0)
                self.SetColorField(COLOR_O, coloursArray[14], 1, 1, 0)
                self.SetColorField(COLOR_P, coloursArray[15], 1, 1, 0)
                f.close()
            except:
                pass

            return True
        #--------------------------------------------------------------------------------------------
        # Default color
        if (id == BUTTON_DEFAULT):
            if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD,c4d.BFM_INPUT_CHANNEL,bc):
                if bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QSHIFT:
                    RemoveLayer()
                    pass
                elif bc[c4d.BFM_INPUT_QUALIFIER] & c4d.QALT:
                    CC = [COLOR_A, COLOR_B, COLOR_C, COLOR_D, COLOR_E, COLOR_F, COLOR_G, COLOR_H, COLOR_I, COLOR_J, COLOR_K, COLOR_L, COLOR_M, COLOR_N, COLOR_O, COLOR_P]
                    colors = []
                    for C in CC:
                        colors.append(self.GetColorField(C)["color"])
                    RandomColor(colors)
                else:
                    try:
                        DefaultColor()
                        RedshiftDefaultColor()

                        try: obj = doc.GetActiveObjects(False)[0]
                        except: tool()[c4d.MDATA_DOODLE_COLOR] = c4d.Vector(1,1,1)
                            
                    except:
                        pass

            return True
        #--------------------------------------------------------------------------------------------
        # Load palette
        if (id == MENU_LOAD):
            fn = s.LoadDialog(c4d.FILESELECTTYPE_ANYTHING,'Select colour palette file',c4d.FILESELECT_LOAD, '')
            if not fn: return True
            f = open(fn.decode("utf-8"))
            coloursArray = []
            for line in f:
                line = line.split(",")
                r = float(line[0])
                g = float(line[1])
                b = float(line[2])
                coloursArray.append(c4d.Vector(r/255.0,g/255.0,b/255.0))
            self.SetColorField(COLOR_A, coloursArray[0], 1, 1, 0)
            self.SetColorField(COLOR_B, coloursArray[1], 1, 1, 0)
            self.SetColorField(COLOR_C, coloursArray[2], 1, 1, 0)
            self.SetColorField(COLOR_D, coloursArray[3], 1, 1, 0)
            self.SetColorField(COLOR_E, coloursArray[4], 1, 1, 0)
            self.SetColorField(COLOR_F, coloursArray[5], 1, 1, 0)
            self.SetColorField(COLOR_G, coloursArray[6], 1, 1, 0)
            self.SetColorField(COLOR_H, coloursArray[7], 1, 1, 0)
            self.SetColorField(COLOR_I, coloursArray[8], 1, 1, 0)
            self.SetColorField(COLOR_J, coloursArray[9], 1, 1, 0)
            self.SetColorField(COLOR_K, coloursArray[10], 1, 1, 0)
            self.SetColorField(COLOR_L, coloursArray[11], 1, 1, 0)
            self.SetColorField(COLOR_M, coloursArray[12], 1, 1, 0)
            self.SetColorField(COLOR_N, coloursArray[13], 1, 1, 0)
            self.SetColorField(COLOR_O, coloursArray[14], 1, 1, 0)
            self.SetColorField(COLOR_P, coloursArray[15], 1, 1, 0)
            f.close()
            return True
        #--------------------------------------------------------------------------------------------
        # Save palette
        if (id == MENU_SAVE):
            CC = [COLOR_A, COLOR_B, COLOR_C, COLOR_D, COLOR_E, COLOR_F, COLOR_G, COLOR_H, COLOR_I, COLOR_J, COLOR_K, COLOR_L, COLOR_M, COLOR_N, COLOR_O, COLOR_P]
            lines = []
            for C in CC:
                line = ""+str(self.GetColorField(C)["color"][0]*255)+","+str(self.GetColorField(C)["color"][1]*255)+","+str(self.GetColorField(C)["color"][2]*255)+""
                lines.append(line)
            lines = "\n".join(lines)
            fn = s.LoadDialog(c4d.FILESELECTTYPE_ANYTHING,'Save colour palette file',c4d.FILESELECT_SAVE, '')
            if not fn: return True
            f = open(fn, 'w')
            f.write(lines)
            f.close()
            return True
        #--------------------------------------------------------------------------------------------
        # Calling presets
        if (id in presetsDict):
            path, fn = os.path.split(__file__)
            fn = os.path.join(path, "presets", presetsDict[id])
            if not fn: return True
            f = open(fn.decode("utf-8"))
            coloursArray = []
            for line in f:
                line = line.split(",")
                r = float(line[0])
                g = float(line[1])
                b = float(line[2])
                coloursArray.append(c4d.Vector(r/255.0,g/255.0,b/255.0))
            self.SetColorField(COLOR_A, coloursArray[0], 1, 1, 0)
            self.SetColorField(COLOR_B, coloursArray[1], 1, 1, 0)
            self.SetColorField(COLOR_C, coloursArray[2], 1, 1, 0)
            self.SetColorField(COLOR_D, coloursArray[3], 1, 1, 0)
            self.SetColorField(COLOR_E, coloursArray[4], 1, 1, 0)
            self.SetColorField(COLOR_F, coloursArray[5], 1, 1, 0)
            self.SetColorField(COLOR_G, coloursArray[6], 1, 1, 0)
            self.SetColorField(COLOR_H, coloursArray[7], 1, 1, 0)
            self.SetColorField(COLOR_I, coloursArray[8], 1, 1, 0)
            self.SetColorField(COLOR_J, coloursArray[9], 1, 1, 0)
            self.SetColorField(COLOR_K, coloursArray[10], 1, 1, 0)
            self.SetColorField(COLOR_L, coloursArray[11], 1, 1, 0)
            self.SetColorField(COLOR_M, coloursArray[12], 1, 1, 0)
            self.SetColorField(COLOR_N, coloursArray[13], 1, 1, 0)
            self.SetColorField(COLOR_O, coloursArray[14], 1, 1, 0)
            self.SetColorField(COLOR_P, coloursArray[15], 1, 1, 0)
            f.close()
            return True
        #--------------------------------------------------------------------------------------------
        # Set as default
        if (id == MENU_SET):
            path, fn = os.path.split(__file__)
            CC = [COLOR_A, COLOR_B, COLOR_C, COLOR_D, COLOR_E, COLOR_F, COLOR_G, COLOR_H, COLOR_I, COLOR_J, COLOR_K, COLOR_L, COLOR_M, COLOR_N, COLOR_O, COLOR_P]
            lines = []
            for C in CC:
                line = ""+str(self.GetColorField(C)["color"][0]*255)+","+str(self.GetColorField(C)["color"][1]*255)+","+str(self.GetColorField(C)["color"][2]*255)+""
                lines.append(line)
            lines = "\n".join(lines)
            fn = os.path.join(path, "res", "default.txt")
            if not fn: return True
            f = open(fn.decode("utf-8"), "w")
            f.write(lines)
            f.close()
            return True
        #--------------------------------------------------------------------------------------------
        # All black
        if (id == MENU_ABLACK):
            coloursArray = []
            for i in range(0,16):
                coloursArray.append(c4d.Vector(0,0,0))

            self.SetColorField(COLOR_A, coloursArray[0], 1, 1, 0)
            self.SetColorField(COLOR_B, coloursArray[1], 1, 1, 0)
            self.SetColorField(COLOR_C, coloursArray[2], 1, 1, 0)
            self.SetColorField(COLOR_D, coloursArray[3], 1, 1, 0)
            self.SetColorField(COLOR_E, coloursArray[4], 1, 1, 0)
            self.SetColorField(COLOR_F, coloursArray[5], 1, 1, 0)
            self.SetColorField(COLOR_G, coloursArray[6], 1, 1, 0)
            self.SetColorField(COLOR_H, coloursArray[7], 1, 1, 0)
            self.SetColorField(COLOR_I, coloursArray[8], 1, 1, 0)
            self.SetColorField(COLOR_J, coloursArray[9], 1, 1, 0)
            self.SetColorField(COLOR_K, coloursArray[10], 1, 1, 0)
            self.SetColorField(COLOR_L, coloursArray[11], 1, 1, 0)
            self.SetColorField(COLOR_M, coloursArray[12], 1, 1, 0)
            self.SetColorField(COLOR_N, coloursArray[13], 1, 1, 0)
            self.SetColorField(COLOR_O, coloursArray[14], 1, 1, 0)
            self.SetColorField(COLOR_P, coloursArray[15], 1, 1, 0)

            return True
        #--------------------------------------------------------------------------------------------
        # Create materials
        if (id == MENU_CRTMAT):
            CC = [COLOR_A, COLOR_B, COLOR_C, COLOR_D, COLOR_E, COLOR_F, COLOR_G, COLOR_H, COLOR_I, COLOR_J, COLOR_K, COLOR_L, COLOR_M, COLOR_N, COLOR_O, COLOR_P]
            colors = []
            for C in CC:
                colors.append(self.GetColorField(C)["color"])
            CreateMaterials(colors)

            return True
        #--------------------------------------------------------------------------------------------
        # Load swatches
        if (id == MENU_LDSW):
            csd = colorchooser.ColorSwatchData(doc)
            grpCount = csd.GetGroupCount(c4d.SWATCH_CATEGORY_DOCUMENT)

            coloursArray = []
            replaceColors = []
            for i in range(0, 16):
                coloursArray.append(c4d.Vector(0,0,0))
            
            for y in range(0, grpCount):
                csg = csd.GetGroupAtIndex(y)
                for y in range(0, csg.GetColorCount()):
                    if csg.IsColorSelected(y):
                        clrs = str(csg.GetColor(y)[0]).split(",")
                        replaceColors.append(c4d.Vector(float(clrs[0]),float(clrs[1]),float(clrs[2])))

            if len(replaceColors) < len(coloursArray):
                rangeAmount = len(replaceColors)
            else:
                rangeAmount = len(coloursArray)

            for k in range(0, rangeAmount):
                coloursArray[k] = replaceColors[k]

            self.SetColorField(COLOR_A, coloursArray[0], 1, 1, 0)
            self.SetColorField(COLOR_B, coloursArray[1], 1, 1, 0)
            self.SetColorField(COLOR_C, coloursArray[2], 1, 1, 0)
            self.SetColorField(COLOR_D, coloursArray[3], 1, 1, 0)
            self.SetColorField(COLOR_E, coloursArray[4], 1, 1, 0)
            self.SetColorField(COLOR_F, coloursArray[5], 1, 1, 0)
            self.SetColorField(COLOR_G, coloursArray[6], 1, 1, 0)
            self.SetColorField(COLOR_H, coloursArray[7], 1, 1, 0)
            self.SetColorField(COLOR_I, coloursArray[8], 1, 1, 0)
            self.SetColorField(COLOR_J, coloursArray[9], 1, 1, 0)
            self.SetColorField(COLOR_K, coloursArray[10], 1, 1, 0)
            self.SetColorField(COLOR_L, coloursArray[11], 1, 1, 0)
            self.SetColorField(COLOR_M, coloursArray[12], 1, 1, 0)
            self.SetColorField(COLOR_N, coloursArray[13], 1, 1, 0)
            self.SetColorField(COLOR_O, coloursArray[14], 1, 1, 0)
            self.SetColorField(COLOR_P, coloursArray[15], 1, 1, 0)

            return True
        #--------------------------------------------------------------------------------------------
        # Create swatches
        if (id == MENU_CRTSW):
            CC = [COLOR_A, COLOR_B, COLOR_C, COLOR_D, COLOR_E, COLOR_F, COLOR_G, COLOR_H, COLOR_I, COLOR_J, COLOR_K, COLOR_L, COLOR_M, COLOR_N, COLOR_O, COLOR_P]
            colors = []
            for C in CC:
                colors.append(self.GetColorField(C)["color"])
            CreateSwatches(colors)

            return True
        #--------------------------------------------------------------------------------------------
        return True
#----------------------------------------------------------------------------------------------------
class Colorise(plugins.CommandData):
  
    dialog = None
    def Execute(self, doc):
        if self.dialog is None:
            self.dialog = MyDialog()
        return self.dialog.Open(dlgtype=c4d.DLG_TYPE_ASYNC, pluginid=PLUGIN_ID, defaultw=400, defaulth=50, xpos=-1, ypos=-1)
		
    def RestoreLayout(self, sec_ref):
        if self.dialog is None:
            self.dialog = MyDialog()
        return self.dialog.Restore(pluginid=PLUGIN_ID, secret=sec_ref)
#----------------------------------------------------------------------------------------------------
# Main
if __name__ == "__main__":
    dir, file = os.path.split(__file__)
    path, fn = os.path.split(__file__)
    bmp = bitmaps.BaseBitmap()
    bmp.InitWith(os.path.join(path, "res", "Icon.tif"))
    plugins.RegisterCommandPlugin(PLUGIN_ID, "Colorise",0, bmp, "Colorise", Colorise())

    