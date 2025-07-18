import maya.cmds as cmds

def subtract_ymin(*objs):
    for obj in objs:
        if cmds.objExists(obj):
            # Get a BBOX attribute
            bbox = cmds.exactWorldBoundingBox(obj)
            min_y = bbox[1]
            
            # Get a World Space Position
            pos = cmds.xform(obj, q=True, ws=True, t=True)
            
            # Subtract min_y
            new_pos = [pos[0], pos[1]-min_y, pos[2]]
            
            # Set xform attribute
            cmds.xform(obj, ws=True, t=new_pos)
        else:
            print(f"'{obj}' is not Exist")