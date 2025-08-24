import copy
import opsc
import oobb
import oobb_base
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "shelf_version_2"

        navigation = True

        #kwargs["save_type"] = "none"        
        #kwargs["save_type"] = "all"
        
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

        screw_diameters = ["m3", "m5_screw_wood"]
        attachment_styles = [""]

        extras = []        
        extras.append("attach_left_side_18_mm_depth_shelf")
        extras.append("attach_right_side_18_mm_depth_shelf")
        extras.append("")

        #version 2
        for screw_diameter in screw_diameters:
            for extra in extras:
                for attachment_style in attachment_styles:                    
                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)
                    p3["width"] = 10
                    p3["height"] = 5
                    p3["thickness"] = 14
                    p3["attachment_style"] = attachment_style
                    ex = extra
                    ex += f"_{screw_diameter}_screw_diameter"
                    if attachment_style != "":
                        ex+= f"_{attachment_style}_attachment_style"
                    p3["extra"] = ex
                    p3["screw_diameter"] = screw_diameter
                    part["kwargs"] = p3
                    part["name"] = "shelf_bracket_version_2"            
                    if attachment_style == "m6_bolt" and extra != "":
                        #skip sides for m6 style
                        pass
                    else:
                        parts.append(part)

                    part = copy.deepcopy(part_default)
                    p3 = copy.deepcopy(kwargs)
                    p3["width"] = 5
                    p3["height"] = 3
                    p3["thickness"] = 14
                    p3["screw_diameter"] = screw_diameter
                    ex = extra
                    ex += f"_{screw_diameter}_screw_diameter"
                    p3["extra"] = ex
                    part["kwargs"] = p3
                    part["name"] = "shelf_bracket_version_2"
                    parts.append(part)

        #obb bracket
        screw_diameters = ["m3", "m5_screw_wood"]
        attachment_styles = ["m6_bolt"]

        sizes = []
        sizes.append([10, 5,14])
        sizes.append([11, 5,14])
        sizes.append([5, 3,21])

        extras = []        
        extras.append("")
        for siz in sizes:
            for screw_diameter in screw_diameters:
                for extra in extras:
                    for attachment_style in attachment_styles:                    
                        wid = siz[0]
                        hei = siz[1]
                        dep = siz[2]
                        part = copy.deepcopy(part_default)
                        p3 = copy.deepcopy(kwargs)
                        p3["width"] = wid
                        p3["height"] = hei
                        p3["thickness"] = dep
                        p3["attachment_style"] = attachment_style
                        ex = extra
                        ex += f"_{screw_diameter}_screw_diameter"
                        if attachment_style != "":
                            ex+= f"_{attachment_style}_attachment_style"
                        p3["extra"] = ex
                        p3["screw_diameter"] = screw_diameter
                        part["kwargs"] = p3
                        part["name"] = "shelf_bracket_version_2"            
                        if attachment_style == "m6_bolt" and extra != "":
                            #skip sides for m6 style
                            pass
                        else:
                            parts.append(part)

                        

        #shelf tops        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 5
        p3["height"] = 7
        p3["thickness"] = 18
        p3["extra"] = extra
        part["kwargs"] = p3
        part["name"] = "shelf_version_2"
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

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        scad_help.generate_navigation(sort = sort)

def get_base(thing, **kwargs):

    #### not the main one anymore

    width = kwargs.get("width", 9)
    height = kwargs.get("height", 9)
    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", True)

    screw_diameter = kwargs.get("screw_diameter", "m3_5")
    screw_shape = "oobb_screw_countersunk"
    if "bolt" in screw_diameter:
        screw_shape = "oobb_bolt"
        screw_diameter = screw_diameter.replace("_bolt", "")
    kwargs["screw_diameter"] = screw_diameter
    kwargs["screw_shape"] = screw_shape


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
        #p3["shape"] = f"oobb_screw_countersunk"
        p3["shape"] = screw_shape
        p3["depth"] = dep
        p3["radius_name"] = screw_diameter
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
        #p3["shape"] = f"oobb_screw_countersunk"
        p3["shape"] = screw_shape
        p3["depth"] = dep
        p3["radius_name"] = "screw_diameter"
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
    screw_diameter = kwargs.get("screw_diameter", "m3")
    #split extra by _ grab the string before _mm_depth_shelf
    if "depth_shelf" in extra:
        depth_shelf = extra.split("_mm_depth_shelf")[0]
        depth_shelf = float(depth_shelf.split("_")[-1])
    else:
        depth_shelf = 0
    #last underscore split string is depth
    screw_diameter = kwargs.get("screw_diameter", "m3_5")
    attachment_style = kwargs.get("attachment_style", "")
    
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
            #moving z depending on side
            if "attach_left" in extra:
                pos1[2] += 0
            elif "attach_right" in extra:
                pos1[2] += depth_endcap
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
            #p3["radius_name"] = "m3d5_screw_wood"
            p3["radius_name"] = screw_diameter
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
            if attachment_style == "m6_bolt":
                shap = f"oobb_hole"
                rad_name = "m6"
            #rad_name = screw_diameter
            hole_extra = 0        
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = shap
            p3["depth"] = dep
            if shap == "oobb_hole":
                p3["depth"] = 20
            p3["radius_name"] = rad_name
            p3["m"] = "#"
            p3["clearance"] = "top"
            pos1 = copy.deepcopy(pos)
            #pos1[1] += ((width/2) * 15) - 0.5 - dep + hole_extra
            shift_horizontal = height/2 * 15 - dep
            pos1[1] += shift_horizontal
            #pos1[0] += 15 * (height - 1)/2 - 15
            pos1[0] += 15 * (width-3)/2
            if shap == "oobb_hole":
                pos1[0] += -60
            
            if shap == "oobb_hole":
                pos1[1] += dep
            pos1[2] += depth/2
            p3["pos"] = pos1
            rot1 = copy.deepcopy(rot)
            rot1[1] += 90
            rot1[2] += -90
            p3["rot"] = rot1
            #rot = [0,90,-90]
            if "side" not in extra:
                oobb_base.append_full(thing,**p3)
                #add loads more for oobb m6 version
                if shap == "oobb_hole" and attachment_style == "m6_bolt":
                    #add the other side
                    shifts  =[15,-15,-30]

                    if width == 11:
                        shifts.append(-45)
                        shifts.append(75)
                        shifts.append(60)
                        shifts.append(45)
                        shifts.append(30)
                    for shift in shifts:
                        p4 = copy.deepcopy(p3)
                        p4["depth"] += -4
                        pos1 = copy.deepcopy(p3["pos"])
                        pos1[0] += shift
                        p4["pos"] = pos1
                        oobb_base.append_full(thing,**p4)
                
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
                if "attach_right" in extra:
                    rot1[1] = 180 
                    pos1[2] += -dep          
                p4["rot"] = rot1
                oobb_base.append_full(thing,**p4)

            p3 = copy.deepcopy(p3)
            pos1 = copy.deepcopy(p3["pos"])
            pos1[0] = pos1[0] - (width-3) * 15
            if shap == "oobb_hole":
                pos1[0] += 60
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
                if "attach_right" in extra:
                    rot1[1] = 180 
                    pos1[2] += -dep   
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

def get_shelf_version_2(thing, **kwargs):

    width = kwargs.get("width", 9)
    width_mm = (width * 15) -1
    height = kwargs.get("height", 9)
    height_mm = (height * 15) -1
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
        p3["shape"] = f"oobb_cube"    
        wid = width*15 - 1
        hei = height*15 - 1
        dep = depth
        size = [wid, hei, dep]
        p3["size"] = size
        pos1 = copy.deepcopy(pos)
        pos1[2] = -depth/2
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
        

    
    
    #add countersunk screws
    if True:
        dep = 16 + 5
        shift_nut = 10
        

        if True:
            shap = f"oobb_screw_countersunk"
            #rad_name = "m3d5_screw_wood"
            rad_name = "m3"
            hole_extra = 0        
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = shap
            p3["depth"] = dep
            p3["radius_name"] = rad_name
            p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[2] += 0
            p3["pos"] = pos1
            rot1 = copy.deepcopy(rot)
            rot1[1] += 90
            rot1[2] += -90
            p3["rot"] = rot1

            p3_nut = copy.deepcopy(kwargs)
            p3_nut["type"] = "n"
            p3_nut["shape"] = f"oobb_nut"
            #p3_nut["depth"] = dep
            p3_nut["radius_name"] = "m3"
            p3_nut["extra_clearance"] = 0.25
            p3_nut["m"] = "#"
            pos1 = copy.deepcopy(pos)            
            pos1[2] += 0
            p3_nut["pos"] = pos1
            rot1 = copy.deepcopy(rot)
            rot1[0] += 90
            rot1[1] += 90
            p3_nut["rot"] = rot1


            #side screws
            if True:
                poss = []
                pos_deets = {}
                pos_deets["shift_width_screw"] = -(width - 3)/2 * 15#-width_mm/2 + 15
                pos_deets["shift_height_screw"] = -height_mm/2 - 5
                pos_deets["rot_screw"] = [0,0,0]
                pos_deets["shift_width_nut"] = pos_deets["shift_width_screw"]
                pos_deets["shift_height_nut"] = -height_mm/2 + shift_nut                
                poss.append(pos_deets)

                pos_deets = {}
                pos_deets["shift_width_screw"] = (width - 3)/2 * 15#-width_mm/2 + 15
                pos_deets["shift_height_screw"] = -height_mm/2 - 5
                pos_deets["rot_screw"] = [0,0,0]
                pos_deets["shift_width_nut"] = pos_deets["shift_width_screw"]
                pos_deets["shift_height_nut"] = -height_mm/2 + shift_nut
                poss.append(pos_deets)

                pos_deets = {}
                pos_deets["shift_width_screw"] = (width - 3)/2 * 15#-width_mm/2 + 15
                pos_deets["shift_height_screw"] = height_mm/2 + 5
                pos_deets["rot_screw"] = [0,0,180]
                pos_deets["shift_width_nut"] = pos_deets["shift_width_screw"]
                pos_deets["shift_height_nut"] = height_mm/2 - shift_nut
                poss.append(pos_deets)

                pos_deets = {}
                pos_deets["shift_width_screw"] = -(width - 3)/2 * 15#-width_mm/2 + 15
                pos_deets["shift_height_screw"] = height_mm/2 + 5
                pos_deets["rot_screw"] = [0,0,180]
                pos_deets["shift_width_nut"] = pos_deets["shift_width_screw"]
                pos_deets["shift_height_nut"] = height_mm/2 - shift_nut
                poss.append(pos_deets)

                for pos_deets in poss:
                    p4 = copy.deepcopy(p3)
                    pos1 = copy.deepcopy(p3["pos"])
                    pos1[0] += pos_deets["shift_width_screw"]
                    pos1[1] += pos_deets["shift_height_screw"]
                    pos1[2] += 0#25
                    p4["pos"] = pos1
                    rot = copy.deepcopy(p3["rot"])
                    rot_screw = pos_deets["rot_screw"]
                    rot[0] += rot_screw[0]
                    rot[1] += rot_screw[1]
                    rot[2] += rot_screw[2]
                    p4["rot"] = rot
                    oobb_base.append_full(thing,**p4)

                    p4_nut = copy.deepcopy(p3_nut)
                    pos1 = copy.deepcopy(p3_nut["pos"])
                    pos1[0] = pos_deets["shift_width_nut"]
                    pos1[1] = pos_deets["shift_height_nut"]
                    pos1[2] += 0#25
                    p4_nut["pos"] = pos1
                    offset_nut = 3
                    repeats = 6
                    for i in range(repeats):
                        p5 = copy.deepcopy(p4_nut)
                        pos1 = copy.deepcopy(p4_nut["pos"])
                        pos1[2] += i * offset_nut
                        p5["pos"] = pos1
                        oobb_base.append_full(thing,**p5)

        


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



    #export kwargs in working.yaml
    import yaml
    working_yaml = "working.yaml"
    with open(working_yaml, 'w') as file:
        yaml.dump(kwargs, file)
    


if __name__ == '__main__':
    kwargs = {}
    kwargs["save_type"] = "none"
    main(**kwargs)