from pymol import cmd

#* CODE RUN

#! Note To User: This only works if you launch VSCode through Anaconda Navigator
#TODO | If on a MacOS: 
# pip install PyQt5
# conda install -c conda-forge -c schrodinger pymol-bundle
#TODO | If on a WinOS: 
# conda install -c conda-forge -c schrodinger pymol-bundle

# Win64: 
"""
run D:\Important Stuff\CODE N' Shi\My_PyMol\PyMol_God_hsba.py
"""

# Darwin:
"""
run /Users/pai.suryadarshan/Desktop/Academics/Year_3/ChemDisease_and_Therapy/CW/My_PyMol/PyMol_God_hsba.py
"""

print("PyMol_God.py imported successfully.")

"""
Decorator used: @cmd.extend

Extend

It is an API-only function which binds a user defined function as a command into the PyMOL scripting language.

Details:
1. All command arguments are passed as strings to the Python function. This may require type conversion before those arguments can be used by the function, for example for numbers (int, float).
2. If the function has a quiet argument, then PyMOL will pass quiet=0 to the command. Most PyMOL core commands have a default quiet=1 argument and have no (or little) output when used in a Python script, but would print a more verbose feedback when invoked as a command.
3. If the function has a _self argument, then PyMOL will assign the global cmd module to _self, or if using the pymol2 module, an instance of pymol2.cmd2.Cmd. This wrapper allows running multiple PyMOL instances in the same process.
"""

@cmd.extend
def hello_world(name="!"):
    print(f"Hello, {name}")
    return

def create_object_from_resi(name, selection):
    cmd.create(str(name), f"resi {selection}")
    return

def extract_object_from_resi(name, selection):
    cmd.extract(str(name), f"resi {selection}")
    return

def create_object_from_selection(name):
    cmd.create(str(name), f"sele")
    return

def select_ligand(selection):
    cmd.select(f"resi {selection}")
    return

def select_water_nearby(radius_of_water = 4):
    cmd.select(f"sele around {radius_of_water} and resn HOH")
    return  

def show_water_nearby(representation_water = "nb_spheres"):
    cmd.show(f"{representation_water}", "sele")
    return

def select_binding_pocket(radius_of_binding = 8):
    cmd.select(f"sele around {radius_of_binding}")
    return

def show_binding_pocket(representation_pocket = "lines"):
    cmd.show(f"{representation_pocket}", "sele")
    return

def hide_obj(Obj_property_to_Hide, Obj_name_to_hide):
    cmd.hide(Obj_property_to_Hide, f"{Obj_name_to_hide}")
    return

def hide_cartoon(representation_to_hide, Obj_whose_cartoon_you_want_to_Hide):
    cmd.hide(f"{representation_to_hide}", Obj_whose_cartoon_you_want_to_Hide)
    return

def delete_obj(obj_name_to_delete):
    cmd.delete(f"{obj_name_to_delete}")
    return

def find_polar_contacts(Name_of_ligand):
    cmd.dist(f"{Name_of_ligand}_polar_conts",f"{Name_of_ligand}",f"(not {Name_of_ligand})",quiet=1,mode=2,label=0,reset=1)
    cmd.enable(f"{Name_of_ligand}_polar_conts")
    return
    

def measure_polar_contacts(Name_of_ligand):
    cmd.show("labels", f"{Name_of_ligand}_polar_conts")
    return


#*### Main ###*#

#* Haylee Style Binding Analysis (HSBA)

@cmd.extend
def hsba():

    #* PARAMETERS

    filename = "protein.pdb"

    Name_of_ligand = "LIG" 
    Ligand_residue_number = 400

    radius_of_binding = 8
    representation_pocket = "lines"

    radius_of_water = 4
    representation_water = "nb_spheres"

    Name_of_Full_binding_pocket = "Binding_pocket"

    Obj_property_to_Hide = "everything"
    Obj_name_to_hide = filename[:-4]

    representation_to_hide = "cartoon"
    Obj_whose_cartoon_you_want_to_Hide = "Binding_pocket"

    Obj_name_to_delete = filename[:-4]

    #* CODE RUN

    extract_object_from_resi(Name_of_ligand, Ligand_residue_number)

    select_ligand(Ligand_residue_number)
    select_water_nearby(radius_of_water)
    show_water_nearby(representation_water)

    select_ligand(Ligand_residue_number)
    select_binding_pocket(radius_of_binding)
    show_binding_pocket(representation_pocket)

    create_object_from_selection(Name_of_Full_binding_pocket)

    hide_obj(Obj_property_to_Hide, Obj_name_to_hide)
    hide_cartoon(representation_to_hide, Obj_whose_cartoon_you_want_to_Hide)

    find_polar_contacts(Name_of_ligand)
    measure_polar_contacts(Name_of_ligand)

    return