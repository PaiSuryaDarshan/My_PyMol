from pymol import cmd
from pymol import util

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

def align(Name_of_obj_1, Name_of_obj_2):
    cmd.align(f"{Name_of_obj_1}",f"{Name_of_obj_2}")
    return

def RMSD(Name_of_obj_1, Name_of_obj_2):
    cmd.align(f"{Name_of_obj_1}",f"{Name_of_obj_2}")
    return

def set_transparency(representation, value, residues):
    cmd.set(f"{representation}_transparency", f"{value}", f"resi {residues}")
    return

def set_color(representation, value):
    cmd.set(f"{representation}_color", f"{value}")
    return

def set_bg_color(value):
    cmd.bg_color(value)
    return

def set_view(view_of_interest):
    cmd.set_view(view_of_interest)
    return

def remove_solvent(solvent_resn):
    cmd.remove(f"resn {solvent_resn}")
    return

################
#*### Main ###*#
################

#* Haylee Style Binding Analysis (HSBA)
@cmd.extend
def hsba(object_name):

    #* PARAMETERS
    #* Default PARAMETERS here
    """
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
    """

    #* Enter PRESET PARAMETERS from Notebook(.ipynb) here
    filename = object_name

    Name_of_ligand = "ADN" 
    Ligand_residue_number = 400

    radius_of_binding = 8
    representation_pocket = "lines"

    radius_of_water = 4
    representation_water = "nb_spheres"

    Name_of_Full_binding_pocket = "Binding_pocket"

    Obj_property_to_Hide = "everything"
    if ".pdb" in filename:
        Obj_name_to_hide = filename[:-4]
    else:
        Obj_name_to_hide = filename

    representation_to_hide = "cartoon"
    Obj_whose_cartoon_you_want_to_Hide = "Binding_pocket"

    if ".pdb" in filename:
        Obj_name_to_delete = filename[:-4]
    else:
        Obj_name_to_delete = filename


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

#* Aligns and orients the same protein but with different ligands
# This function is EXCELLENT for creating consistently aigned images <3
@cmd.extend
def align_and_orient(obj_1, obj_2):

    """
    Align the ligand to the protein,
    and orient the protein to show ligand of interest
    (Keeps the orientation consistent)
    """

    Name_of_obj_1 = obj_1
    Name_of_obj_2 = obj_2


    #* Enter PRESET PARAMETERS from Notebook(.ipynb) here

    representation_to_hide = "cartoon"
    Obj_whose_cartoon_you_want_to_Hide = "resi 266-291"

    view_of_interest = "(\
     0.371393293,    0.304631203,   -0.877057135,\
     0.424994588,   -0.895621717,   -0.131108478,\
    -0.825472653,   -0.324035168,   -0.462101817,\
    -0.001281321,   -0.000470711,  -39.313049316,\
    31.598876953,    9.013586998,  -16.942543030,\
  -375.424896240,  455.384063721,  -20.000000000 )"

    
    #* CODE RUN

    align(Name_of_obj_1, Name_of_obj_2)

    hide_cartoon(representation_to_hide, Obj_whose_cartoon_you_want_to_Hide)
    remove_solvent("SOG")  

    set_color("cartoon", "white")
    set_bg_color("white")

    set_view(view_of_interest)
    
    return