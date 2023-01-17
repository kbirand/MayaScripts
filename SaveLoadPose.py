import json
from collections import OrderedDict
from pymel.core import Path

def saveJSONPose():
    jnts = pm.selected()
    jnts = pm.ls(type="joint")

    jnts = sorted(jnts)
    poseDict = OrderedDict()
    for jnt in jnts:
        r = list(jnt.rotate.get())
        poseDict[jnt.nodeName()] = {'r':r}

    print(poseDict)
    poseFilePath = r"C:\koray\poseA2.json"
    with open(poseFilePath,'w') as p:
        json.dump(poseDict,p,indent=4)

def loadJSONPose():
    
    poseFilePath = r"C:\koray\poseA2.json"
    poseData = json.load(open(poseFilePath))

    for j,v in poseData.items():
        for c,vals in v.items():
            print("{0}: {1}".format(c,vals))
            j = pm.PyNode(j)
            j.attr(c).set(vals)
        
#saveJSONPose()
loadJSONPose()
