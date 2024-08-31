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
        #filter = "test"

        #kwargs["save_type"] = "none"
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
        part["kwargs"] = p3
        part["name"] = "base"
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