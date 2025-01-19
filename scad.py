import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        filter = "shelf_bracket_version_2"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 7
        kwargs["height"] = 7
        kwargs["thickness"] = 12

    # project_variables
    if True:
        pass
    
    # declare parts
    if True:
        part_default = {} 
        part_default["project_name"] = "oomlout_oobb_organizing_shelf_bracket" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        p3["extra"] = "m6_holes"
        part["kwargs"] = p3
        part["name"] = "shelf_bracket"
        
        parts.append(part)

        #version 2
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 10
        p3["height"] = 5
        p3["thickness"] = 14
        p3["extra"] = "attach_side_18_mm_depth_shelf"
        part["kwargs"] = p3
        part["name"] = "shelf_bracket_version_2"
        
        parts.append(part)

        part = copy.deepcopy(part)
        part["kwargs"]["extra"] = ""
        parts.append(part)

    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_base(thing, **kwargs):

    width = kwargs.get("width", 9)
    height = kwargs.get("height", 9)
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    if True:
        #add holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = "single"
        locs = []

        skip_rows = [width-1, width-3]
        skip_cols = [2, 4]
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols:
                    locs.append([i,j])
        p3["loc"] = locs
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #add holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        p3["holes"] = "single"
        locs = []
        skip_rows = [1]
        skip_cols = [2, 4]
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols:
                    locs.append([i,j])
        p3["loc"] = locs
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[0] += -15/2
        pos1[1] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        locs = []
        skip_rows = [height-1, height - 3]
        skip_cols = [width - 2]
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols:
                    locs.append([i,j])
        p3["loc"] = locs        
        pos1 = copy.deepcopy(pos)        
        pos1[1] += -15/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #add countersunk screws
    if True:
        dep = 15
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = dep
        p3["radius_name"] = "m3d5_screw_wood"
        p3["m"] = "#"
        p3["clearance"] = "top"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (-(width/2) * 15) + 0.5 + dep
        pos1[1] += -15 * (height - 1)/2 + 15
        pos1[2] += depth/2
        p3["pos"] = pos1
        rot = [0,90,0]
        p3["rot"] = rot
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])
        pos1[1] = pos1[1] + 30
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = dep
        p3["radius_name"] = "m3d5_screw_wood"
        p3["m"] = "#"
        p3["clearance"] = "top"
        pos1 = copy.deepcopy(pos)
        pos1[1] += ((width/2) * 15) - 0.5 - dep
        pos1[0] += 15 * (height - 1)/2 - 15
        pos1[2] += depth/2
        p3["pos"] = pos1
        rot = [0,90,-90]
        p3["rot"] = rot
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])
        pos1[0] = pos1[0] - 30
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)





    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        #thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        p3["rot"] = [0,0,-45]
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_shelf_bracket(thing, **kwargs):

    width = kwargs.get("width", 9)
    height = kwargs.get("height", 9)
    depth = kwargs.get("thickness", 4)
    extra = kwargs.get("extra", "")
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    if True:
        #add holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = "single"
        locs = []

        skip_rows = [width-1, width-3]
        skip_cols = [2, 4]
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols:
                    locs.append([i,j])
        p3["loc"] = locs
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #add holes
        # m3 in line with big holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        p3["holes"] = "single"
        locs = []
        skip_rows = [1,height]
        skip_cols = [2, 4]
        skip_coords = []
        skip_coords.append([2,1])
        skip_coords.append([4,3])
        skip_coords.append([6,5])
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols and [i,j] not in skip_coords:
                    locs.append([i,j])
        p3["loc"] = locs
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[0] += -15/2
        pos1[1] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        locs = []
        skip_rows = [height-1, height - 3, height]
        skip_cols = [width - 2,1]
        skip_coords = []
        skip_coords.append([2,2])
        skip_coords.append([3,3])
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols and [i,j] not in skip_coords:
                    locs.append([i,j])
        p3["loc"] = locs        
        pos1 = copy.deepcopy(pos)        
        pos1[1] += -15/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #add countersunk screws
    if True:
        dep = 15
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["depth"] = dep
        p3["radius_name"] = "m3d5_screw_wood"
        p3["m"] = "#"
        p3["clearance"] = "top"
        pos1 = copy.deepcopy(pos)
        pos1[0] += (-(width/2) * 15) + 0.5 + dep
        pos1[1] += -15 * (height - 1)/2 + 15
        pos1[2] += depth/2
        p3["pos"] = pos1
        rot = [0,90,0]
        p3["rot"] = rot
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])
        pos1[1] = pos1[1] + 30
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        shap = f"oobb_screw_countersunk"
        rad_name = "m3d5_screw_wood"
        hole_extra = 0
        if extra == "m6_holes":
            shap = f"oobb_hole"
            rad_name = "m6"
            hole_extra = 400
            dep = 250
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = shap
        p3["depth"] = dep
        p3["radius_name"] = rad_name
        p3["m"] = "#"
        p3["clearance"] = "top"
        pos1 = copy.deepcopy(pos)
        pos1[1] += ((width/2) * 15) - 0.5 - dep + hole_extra
        pos1[0] += 15 * (height - 1)/2 - 15
        pos1[2] += depth/2
        p3["pos"] = pos1
        rot = [0,90,-90]
        p3["rot"] = rot
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        pos1 = copy.deepcopy(p3["pos"])
        pos1[0] = pos1[0] - 30
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)



    #add step cutout
    if True:
        #for width
        for i in range(1,width+1):
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_plate"    
            p3["depth"] = depth
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[1] += -((width-i) * 15 )
            pos1[0] += (i) * 15
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
        


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        #thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        p3["rot"] = [0,0,-45]
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_shelf_bracket_version_2(thing, **kwargs):

    width = kwargs.get("width", 9)
    height = kwargs.get("height", 9)
    depth = kwargs.get("thickness", 4)
    extra = kwargs.get("extra", "")
    #split extra by _ grab the string before _mm_depth_shelf
    if "depth_shelf" in extra:
        depth_shelf = extra.split("_mm_depth_shelf")[0]
        depth_shelf = float(depth_shelf.split("_")[-1])
    else:
        depth_shelf = 0
    #last underscore split string is depth
    
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    rot = kwargs.get("rot", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20


    #add plate 
    if True:
        #long plate width
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"    
        p3["width "] = width
        hei = 1
        if "side" in extra:
            hei += depth_shelf / 15
        p3["height"] = hei 
        p3["depth"] = depth    
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[1] += (height-1) / 2 * 15 + depth_shelf / 2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
    
        #short plate height
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"    
        p3["width"] = 1
        #p3["height"] = height
        p3["depth"] = depth    
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[0] += -(width-1) / 2 * 15
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #joining plate hypothenuse
        import math
        width_mm = (width-1) * 15
        height_mm = (height-1) * 15
        #calculate the length of the hypotenuse
        hypotenuse = math.sqrt(width_mm**2 + height_mm**2)
        wid_mm = width_mm
        #calculate angle
        angle = math.degrees(math.atan(height_mm / width_mm))
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_plate"
        p3["width"] = (hypotenuse + 10) / 15
        p3["height"] = 1
        p3["depth"] = depth
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0#wid_mm / 2
        pos1[1] += 0#height_mm / 2
        p3["pos"] = pos1
        
        rot1  = copy.deepcopy(rot)
        rot1[2] = angle
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)


    #add shelf cutout
    depth_endcap = 3
    if True:
        if depth_shelf > 0:
            
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_cube"
            wid = width*15 - 1
            hei = 18
            dep = depth - depth_endcap
            size = [wid, hei, dep]
            p3["size"] = size
            pos1 = copy.deepcopy(pos)
            pos1[0] += 0
            pos1[1] += depth_shelf/2 + height*15/2
            pos1[2] += 0
            p3["pos"] = pos1
            #p3["m"] = "#"   
            oobb_base.append_full(thing,**p3)


    if False:
        #add holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["holes"] = "single"
        locs = []

        skip_rows = [width-1, width-3]
        skip_cols = [2, 4]
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols:
                    locs.append([i,j])
        p3["loc"] = locs
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #add holes
        # m3 in line with big holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_holes"
        p3["both_holes"] = True  
        p3["depth"] = depth
        p3["radius_name"] = "m3"
        p3["holes"] = "single"
        locs = []
        skip_rows = [1,height]
        skip_cols = [2, 4]
        skip_coords = []
        skip_coords.append([2,1])
        skip_coords.append([4,3])
        skip_coords.append([6,5])
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols and [i,j] not in skip_coords:
                    locs.append([i,j])
        p3["loc"] = locs
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)         
        pos1[0] += -15/2
        pos1[1] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        p3 = copy.deepcopy(p3)
        locs = []
        skip_rows = [height-1, height - 3, height]
        skip_cols = [width - 2,1]
        skip_coords = []
        skip_coords.append([2,2])
        skip_coords.append([3,3])
        for i in range(1,width+1):
            for j in range(1,height+1):
                if i not in skip_rows and j not in skip_cols and [i,j] not in skip_coords:
                    locs.append([i,j])
        p3["loc"] = locs        
        pos1 = copy.deepcopy(pos)        
        pos1[1] += -15/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    #add countersunk screws
    if True:
        dep = 14
        #short side wall side screws
        if True:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_screw_countersunk"
            p3["depth"] = dep
            p3["radius_name"] = "m3d5_screw_wood"
            p3["m"] = "#"
            p3["clearance"] = "top"
            pos1 = copy.deepcopy(pos)
            pos1[0] += (-(width/2) * 15) + 0.5 + dep
            #pos1[1] += -15 * (height - 1)/2 + 15
            pos1[1] += -15 * (height - 1)/2
            pos1[2] += depth/2
            p3["pos"] = pos1
            rot1 = copy.deepcopy(rot)
            rot1[1] += 90
            #rot = [0,90,0]
            p3["rot"] = rot1
            oobb_base.append_full(thing,**p3)

            p3 = copy.deepcopy(p3)
            pos1 = copy.deepcopy(p3["pos"])
            pos1[1] = pos1[1] + (height -2)* 15
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)

        if True:
            shap = f"oobb_screw_countersunk"
            rad_name = "m3d5_screw_wood"
            hole_extra = 0        
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = shap
            p3["depth"] = dep
            p3["radius_name"] = rad_name
            p3["m"] = "#"
            p3["clearance"] = "top"
            pos1 = copy.deepcopy(pos)
            #pos1[1] += ((width/2) * 15) - 0.5 - dep + hole_extra
            shift_horizontal = height/2 * 15 - dep
            pos1[1] += shift_horizontal
            #pos1[0] += 15 * (height - 1)/2 - 15
            pos1[0] += 15 * (width-3)/2
            pos1[2] += depth/2
            p3["pos"] = pos1
            rot1 = copy.deepcopy(rot)
            rot1[1] += 90
            rot1[2] += -90
            p3["rot"] = rot1
            #rot = [0,90,-90]
            if "side" not in extra:
                oobb_base.append_full(thing,**p3)
            shift_vertical = 14 + depth_shelf/2
            shift_z = depth/2
            if "side" in extra:
                p4 = copy.deepcopy(p3)
                pos1 = copy.deepcopy(p3["pos"])
                pos1[0] = (width-3)/2 * 15
                pos1[1] += shift_vertical
                pos1[2] += shift_z
                p4["pos"] = pos1
                rot1 = copy.deepcopy(rot)
                rot1[1] = 0                
                p4["rot"] = rot1
                oobb_base.append_full(thing,**p4)

            p3 = copy.deepcopy(p3)
            pos1 = copy.deepcopy(p3["pos"])
            pos1[0] = pos1[0] - (width-3) * 15
            p3["pos"] = pos1
            if "side" not in extra:
                oobb_base.append_full(thing,**p3)
            if "side" in extra:
                p4 = copy.deepcopy(p3)
                pos1 = copy.deepcopy(p3["pos"])
                pos1[0] = -(width-3)/2 * 15
                pos1[1] += shift_vertical
                pos1[2] += shift_z
                p4["pos"] = pos1
                rot1 = copy.deepcopy(rot)
                rot1[1] = 0                
                p4["rot"] = rot1
                oobb_base.append_full(thing,**p4)



    #add step cutout
    if False:
        #for width
        for i in range(1,width+1):
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_plate"    
            p3["depth"] = depth
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)         
            pos1[1] += -((width-i) * 15 )
            pos1[0] += (i) * 15
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)
        


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        #thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        p3["rot"] = [0,0,-45]
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)