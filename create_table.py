import maya.cmds as cmds

def create_table(table_size_x, table_size_y, table_size_z, leg_size_x, leg_size_y, leg_size_z, x_bias, z_bias):
    # Check a condition
    if not cmds.objExists('table'):
        # Make a Top
        top = cmds.polyCube(n = 'top')[0]
        cmds.setAttr(top + '.scale', table_size_x, table_size_y, table_size_z, type = 'double3')
        # Make a Ref Leg named "leg0"
        leg0 = cmds.polyCube(n = 'leg0')[0]
        cmds.setAttr(leg0 + '.scale', leg_size_x, leg_size_y, leg_size_z, type = 'double3')
        cmds.move(table_size_x*0.5*x_bias, (-leg_size_y-table_size_y)*0.5, table_size_z*0.5*z_bias, leg0, relative=True)
        # Duplicate a leg
        leg1 = cmds.duplicate('leg0')[0]
        cmds.setAttr(leg1 + '.translate', -table_size_x*0.5*x_bias, (-leg_size_y-table_size_y)*0.5, table_size_z*0.5*z_bias, type = 'double3')
        # Duplicate a legs
        leg2, leg3 = cmds.duplicate('leg0', 'leg1')
        cmds.setAttr(leg2 + '.translate', table_size_x*0.5*x_bias, (-leg_size_y-table_size_y)*0.5, -table_size_z*0.5*z_bias, type = 'double3')
        cmds.setAttr(leg3 + '.translate', -table_size_x*0.5*x_bias, (-leg_size_y-table_size_y)*0.5, -table_size_z*0.5*z_bias, type = 'double3')
        # Grouping
        cmds.group(top, leg0, leg1, leg2, leg3, n='table')
    else:
        cmds.error("Error : Table is exist")
