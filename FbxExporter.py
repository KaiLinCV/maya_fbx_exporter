# This python script for Maya will export selected objects in the scene into fbx exports.
# Script by: Kai-Lin Chuang

import maya.cmds as cmds
import maya.mel as mm
import os

def CreateWindow():

    # If window exists, close the current window and re-open a new one.
    if cmds.window("FbxExport", ex=True):
        cmds.deleteUI("FbxExport")
    
    #create window
    cmds.window("FbxExport", title="Fbx Exporter", widthHeight=(300,300), s=True, menuBar=True)
    cmds.window("FbxExport", edit=True, widthHeight=(300,84), backgroundColor=[0.25,0.25,0.25])
    cmds.columnLayout(adjustableColumn=True)

    cmds.frameLayout(label='Export to Folder', backgroundShade=True, backgroundColor=[0.5,0.5,0.5])
    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=([1,316]))

    cmds.rowColumnLayout(numberOfColumns=1, columnWidth=([1,315]))
    cmds.textField("FilePath", text="", pht="Please select a folder", ed=True, dif=True,
                   editable=True, backgroundColor=[0.3,0.3,0.3], h=24)
    cmds.setParent("..")

    #Export, show and select folder buttons
    cmds.rowColumnLayout(numberOfColumns=3, columnWidth=([1,200],[2,32],[3,32]))
    cmds.button(label="Export",c=ExportPoly, ann="Export Selected Objects")
    cmds.iconTextButton( style='iconOnly', h=24, image1="folder-new.png", c=GetDir, ann="Select folder for exporting" )
    cmds.iconTextButton( style='iconOnly', h=24, image1="folder-open.png", c=ShowDir, ann="Show selected folder" )
    cmds.setParent("..")

    cmds.setParent("..")
    cmds.setParent("..")
    cmds.showWindow("FbxExport")

# Gets the directory to export files into
def GetDir(*args):
    getdir = cmds.fileDialog2(fm=3, okc='Select Folder')[0]
    cmds.textField("FilePath", e=True, tx=getdir)

# Show directory folder
def ShowDir(*args):
    showdir = cmds.textField("FilePath", q=True, tx=True)
    if showdir:
        os.startfile(showdir)
    else:
        cmds.confirmDialog(t='Info',icon="information",m="Please select a Folder",button='OK')

# Export the selected into fbx files
def ExportPoly(*args):
    polySel = cmds.ls(sl=True)
    for object in polySel:
        if object:
            path = cmds.textField("FilePath",q=True,tx=True)

            cmds.select(object)
            objectNames = cmds.ls(sl=True)
            splitName = objectNames[0].split('|')
            objectName = splitName[-1]

            exportPath = path + '/' + objectName + '.fbx'
            cmds.file(exportPath, es=True, force=True, type="FBX export", pr=True)

# Run the create window function
CreateWindow()
