def hard_edges(min_angle, max_angle):
    selected = cmds.ls(selection=True)    

    # First object of selected
    if selected:
        obj = selected[0]
    
        # Obj is Exist
        if cmds.objExists(obj):
            # Select All Edges
            cmds.select(obj + ".e[*]", r=True)
            # Set a polySelectConstraint
            mel.eval(f'polySelectConstraint -m 2 -t 0x8000 -a 1 -ab {min_angle} {max_angle};')
            # Clear a polySelectConstraint
            mel.eval('polySelectConstraint -m 0;')
            
            print("Hard edges selected for:", obj_name)