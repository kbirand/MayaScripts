import maya.cmds as cmds
avatar = 'BP_CM_Alejandra'
sub = '|Body|root'
sub2 = '|Face|root'

cmds.select(d=True)
final = avatar + sub
final2 = avatar + sub2
myData = []
myJoints = {}

cmds.select(final, hi=True)

selected = cmds.ls(sl=True,long=True) or []

for eachSel in selected:
    bone = (eachSel.split('|')[-1])
    
    pos1 = cmds.xform(eachSel, query=True, worldSpace=False, rotation=True)
    myJoints[bone] = pos1
    myData.append(pos1)

cmds.select(d=True)
cmds.select(final2, hi=True)
selected2 = cmds.ls(sl=True,long=True) or []



for eachSel in selected2:
    bone = (eachSel.split('|')[-1])
    if bone in myJoints:
        cmds.rotate(myJoints[bone][0],myJoints[bone][1],myJoints[bone][2], eachSel)
   

