from pymol import cmd
from pymol import util

# Pai is the best :sunglasses:

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

def side_chain_only_from_resi(residues_of_interest, representation_side_chain = "sticks"):
    cmd.show(representation_side_chain, f"((byres (resi {residues_of_interest}))&(sc.|(n. CA|n. N&r. PRO)))")
    return

def side_chain_only_from_obj(obj_of_interest, representation_side_chain = "sticks"):
    cmd.show(representation_side_chain, f"((byres ({obj_of_interest}))&(sc.|(n. CA|n. N&r. PRO)))")
    return

def hide_obj(Obj_property_to_Hide, Obj_name_to_hide):
    cmd.hide(Obj_property_to_Hide, f"{Obj_name_to_hide}")
    return

def hide_cartoon(Obj_whose_cartoon_you_want_to_Hide):
    cmd.hide("cartoon", Obj_whose_cartoon_you_want_to_Hide)
    return

def delete_obj(obj_name_to_delete):
    cmd.delete(f"{obj_name_to_delete}")
    return

def set_new_hbond_cutoff():
    cmd.set("h_bond_cutoff_center", 3.7)
    cmd.set("h_bond_cutoff_edge", 3.7)
    return

def find_polar_contacts(Name_of_ligand):
    set_new_hbond_cutoff()
    cmd.dist(f"{Name_of_ligand}_polar_conts",f"{Name_of_ligand}",f"(not {Name_of_ligand})",quiet=1,mode=2,label=0,reset=1)
    cmd.dist(f"{Name_of_ligand}_pipi_conts",f"{Name_of_ligand}",f"(not {Name_of_ligand})",quiet=1,mode=6,label=0,reset=1)
    cmd.enable(f"{Name_of_ligand}_polar_conts")
    return

def measure_polar_contacts(Name_of_ligand):
    cmd.show("labels", f"{Name_of_ligand}_polar_conts")
    cmd.show("labels", f"{Name_of_ligand}_pipi_conts")
    return

def align(Name_of_obj_1, Name_of_obj_2):
    cmd.align(f"{Name_of_obj_1}",f"{Name_of_obj_2}")
    return

def RMSD(Name_of_obj_1, Name_of_obj_2):
    cmd.align(f"{Name_of_obj_1}",f"{Name_of_obj_2}")
    return

def set_transparency(representation, value, residues=""):
    if residues != "":
        cmd.set(f"{representation}_transparency", value, f"resi {residues}")
    else:
        cmd.set(f"{representation}_transparency", value)
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
def hsba(object_name, Name_of_ligand = "Lig"):

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
    hide_cartoon(Obj_whose_cartoon_you_want_to_Hide)
    hide_cartoon(Name_of_Full_binding_pocket)

    find_polar_contacts(Name_of_ligand)
    measure_polar_contacts(Name_of_ligand)

    return

@cmd.extend
def hsba_SwissDock(Ligand_name, Name_of_ligand = "Lig"):

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
    filename = "irrelevant"

    Name_of_ligand = Name_of_ligand 
    Ligand_residue_number = 1

    radius_of_binding = 8
    representation_pocket = "lines"

    radius_of_water = 4
    representation_water = "nb_spheres"

    Name_of_Full_binding_pocket = "Binding_pocket"

    Obj_property_to_Hide = "everything"

    Obj_name_to_hide = "group01"

    representation_to_hide = "cartoon"
    Obj_whose_cartoon_you_want_to_Hide = "Binding_pocket"

    if ".pdb" in filename:
        Obj_name_to_delete = filename[:-4]
    else:
        Obj_name_to_delete = filename

    #* CODE RUN

    cmd.group(cmd.get_unused_name("group01"),f"{Ligand_name}, receptor",quiet=0)

    extract_object_from_resi(Name_of_ligand, Ligand_residue_number)

    select_ligand(Ligand_residue_number)
    select_water_nearby(radius_of_water)
    show_water_nearby(representation_water)

    select_ligand(Ligand_residue_number)
    select_binding_pocket(radius_of_binding)
    show_binding_pocket(representation_pocket)

    create_object_from_selection(Name_of_Full_binding_pocket)

    cmd.hide("((byres (Binding_pocket))&(bb.&!(n. CA|n. N&r. PRO)))")
    cmd.select("main", "resi 88+168+169+250+253+277+278")

    hide_obj(Obj_property_to_Hide, Obj_name_to_hide)
    hide_cartoon(Obj_whose_cartoon_you_want_to_Hide)

    find_polar_contacts(Name_of_ligand)
    measure_polar_contacts(Name_of_ligand)

    cmd.select("main", "resi 88+168+169+250+253+277+278")

    return

#* Aligns and orients the same protein but with different ligands
# This function is EXCELLENT for creating consistently aigned images <3
@cmd.extend
def align_and_orient(obj_1, obj_2=""):

    """
    Align the protein to another protein,
    and orient the protein to show ligand of interest
    (Keeps the orientation consistent)
    """

    Name_of_obj_1 = obj_1
    Name_of_obj_2 = obj_2


    #* Enter PRESET PARAMETERS from Notebook(.ipynb) here

    representation_to_hide = "cartoon"
    Obj_whose_cartoon_you_want_to_Hide = "resi 266-291"

    aligned_view_of_interest = "(\
     0.371393293,    0.304631203,   -0.877057135,\
     0.424994588,   -0.895621717,   -0.131108478,\
    -0.825472653,   -0.324035168,   -0.462101817,\
    -0.001281321,   -0.000470711,  -39.313049316,\
    31.598876953,    9.013586998,  -16.942543030,\
  -375.424896240,  455.384063721,  -20.000000000 )"
    
    singular_view_of_interest = "(\
    -0.287070036,   -0.255746454,    0.923137307,\
     0.477690846,   -0.873542368,   -0.093456171,\
     0.830299854,    0.414147615,    0.372936934,\
    -0.000029288,    0.000003709,  -38.392292023,\
   -29.723110199,    8.598756790,  -22.384565353,\
  -6225.533691406, 6302.318359375,  -20.000000000 )"
    
    #* CODE RUN
    if Name_of_obj_2 != "":
        align(Name_of_obj_1, Name_of_obj_2)
        set_view(aligned_view_of_interest)
    else:
        set_view(singular_view_of_interest)

    hide_cartoon(Obj_whose_cartoon_you_want_to_Hide)
    remove_solvent("SOG")  

    set_color("cartoon", "white")
    set_bg_color("white")

    
    
    return

@cmd.extend 
def align_and_orient_2(obj_1, obj_2=""):

    """
    Align the protein to another protein,
    and orient the protein to show ligand of interest
    (Keeps the orientation consistent)
    """

    Name_of_obj_1 = obj_1
    Name_of_obj_2 = obj_2


    #* Enter PRESET PARAMETERS from Notebook(.ipynb) here

    representation_to_hide = "cartoon"
    Obj_whose_cartoon_you_want_to_Hide = "resi 266-291"

    aligned_view_of_interest = "(\
     0.371393293,    0.304631203,   -0.877057135,\
     0.424994588,   -0.895621717,   -0.131108478,\
    -0.825472653,   -0.324035168,   -0.462101817,\
    -0.001281321,   -0.000470711,  -39.313049316,\
    31.598876953,    9.013586998,  -16.942543030,\
  -375.424896240,  455.384063721,  -20.000000000 )"
    
    singular_view_of_interest = "(\
    -0.576076627,    0.032612275,    0.816744387,\
     0.554881990,   -0.718096852,    0.420050710,\
     0.600199580,    0.695178926,    0.395583093,\
     0.000000000,    0.000000000,  -54.548500061,\
   -29.258552551,    8.441627502,  -22.931236267,\
  -79972.296875000, 80081.390625000,  -20.000000000 )"
    
#     (\
#     -0.575957119,   -0.194436401,    0.794018865,\
#      0.556095123,   -0.805127919,    0.206219062,\
#      0.599189520,    0.560324311,    0.571845293,\
#      0.000000000,    0.000000000,  -54.548500061,\
#    -29.258552551,    8.441627502,  -22.931236267,\
#   -79972.296875000, 80081.390625000,  -20.000000000 )
    
    #* CODE RUN
    if Name_of_obj_2 != "":
        align(Name_of_obj_1, Name_of_obj_2)
        set_view(aligned_view_of_interest)
    else:
        set_view(singular_view_of_interest)

    hide_cartoon(Obj_whose_cartoon_you_want_to_Hide)
    remove_solvent("SOG")  

    set_color("cartoon", "white")
    set_bg_color("white")

    
    
    return
 
@cmd.extend
def show_interacting_residues(residues_of_interest, Obj_of_interest, new_obj_name = "interactions", transparency_of_sticks=0.5):

    """
    Shows all interacting residues / residues of choice
    Shows it as sticks, colors it by atom where carbon = white
    Sets transparency of sticks to that of choice
    (this last thing helps see through any obstruting structures)

    residues_of_interest: string | res1+res2+res3
    objects_of_interest: string | ABC
    """

    # 253+278+277+168+169
    obj_name = new_obj_name
    residues_of_interest = residues_of_interest
    Obj_of_interest = Obj_of_interest
    trans= transparency_of_sticks

    # * Code Run
    cmd.create(f"{obj_name}", f"resi {residues_of_interest} and {Obj_of_interest}")
    side_chain_only_from_obj(f"{obj_name}")
    hide_cartoon(f"{obj_name}")
    util.cbaw(f"{obj_name}") 
    cmd.set("stick_transparency", trans, f"{obj_name}")

    return

@cmd.extend
def label_interactions_obj(obj_name="interactions"):

    #* Aligns and orients the same protein but with different ligands
    # This function is EXCELLENT for creating consistently aigned images <3

    """
    Labels stuff the way I like it for quick ref.
    """
    cmd.label(f'''(name CA+C1*+C1' and (byres({obj_name})))''','''"%s%s"%(resn,resi)''')
    
    return

@cmd.extend
def pai_style(representation_side_chain, residues_of_interest):
    cmd.show(representation_side_chain, f"((byres ({residues_of_interest}))&(sc.|(n. CA|n. N&r. PRO)))")
    cmd.label(f'''(name CA+C1*+C1' and (byres({residues_of_interest})))''','''"%s%s"%(resn,resi)''')
    set_transparency("cartoon", 0.9)
    util.cnc(residues_of_interest)
    return

@cmd.extend
def SPF(object_name):

    """
    Show Pharmacaphore Fingerprint

    """

    residues_of_interest = "253+278+277+168+169+88"

    show_interacting_residues(residues_of_interest, f"{object_name}", "fingerprint")    
    label_interactions_obj("fingerprint")

    return  

@cmd.extend
def pai_save(save_name):
    cmd.png(f"/Users/pai.suryadarshan/Downloads/{save_name}.png", width=0, height=0, dpi=-1, ray=0, quiet=0)
    return