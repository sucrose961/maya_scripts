def set_pivot_to_bottom(*objs):
    for obj in objs:
        if cmds.objExists(obj):
            # Get a BBOX attribute
            bbox = cmds.exactWorldBoundingBox("R_Cube")

            # Calculate a x_center and a z_center
            x_center = (bbox[0] + bbox[3]) * 0.5
            y_min = bbox[1]
            z_center = (bbox[2] + bbox[5]) * 0.5
            
            # Set a new Pivot Position
            new_pivot_pos = [x_center, y_min, z_center]

            # Activate
            cmds.xform(obj, piv=new_pivot_pos, ws=True)
        else:
            print(f"'{obj}' is not Exist")