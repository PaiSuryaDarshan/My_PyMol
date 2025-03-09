from pymol import cmd
from pymol import util

# * Preamble
util.performance(0) # Set max quality

#TODO: Import Color-blind safe pallete

cmd.set_color("cb_black",           [0, 0, 0],      quiet=0)
cmd.set_color("cb_orange",          [230, 159, 0],  quiet=0)
cmd.set_color("cb_sky_blue",        [86, 180, 233], quiet=0)
cmd.set_color("cb_bluish_green",    [0, 158, 115],  quiet=0)
cmd.set_color("cb_yellow",          [240, 228, 66], quiet=0)
cmd.set_color("cb_blue",            [0, 114, 178],  quiet=0)
cmd.set_color("cb_vermillion",      [213, 94, 0],   quiet=0)
cmd.set_color("cb_redpurple",       [204, 121, 167],quiet=0)

def set_transparency(representation, value, residues=""):
    if residues != "":
        cmd.set(f"{representation}_transparency", value, f"resi {residues}")
    else:
        cmd.set(f"{representation}_transparency", value)
    return

def set_color(representation, value):
    cmd.set(f"{representation}_color", f"{value}")


# * Views
@cmd.extend
def pai_view_1():

    """
    View Angle Preset 1
    """
    
    singular_view_of_interest = "(\
    -0.287070036,   -0.255746454,    0.923137307,\
     0.477690846,   -0.873542368,   -0.093456171,\
     0.830299854,    0.414147615,    0.372936934,\
    -0.000029288,    0.000003709,  -48.635307312,\
   -29.723110199,    8.598756790,  -22.384565353,\
  -6215.290527344, 6312.561523438,  -20.000000000 )"
    
    #* CODE RUN
    cmd.set_view(singular_view_of_interest)
    cmd.hide("sticks", "resi 270+274")
    return

@cmd.extend 
def pai_view_2():

    """
    View Angle Preset 2
    """
    
    singular_view_of_interest = "(\
    -0.576076627,    0.032612275,    0.816744387,\
     0.554881990,   -0.718096852,    0.420050710,\
     0.600199580,    0.695178926,    0.395583093,\
     0.000000000,    0.000000000,  -54.548500061,\
   -29.258552551,    8.441627502,  -22.931236267,\
  -79972.296875000, 80081.390625000,  -20.000000000 )"
    
    #* CODE RUN
    cmd.set_view(singular_view_of_interest)
    cmd.hide("sticks", "resi 270+274")
    return

@cmd.extend
def pai_view_3():

    """
    View Angle Preset 3
    """
    
    singular_view_of_interest = "(\
    -0.304608017,   -0.424645096,    0.852577507,\
     0.491963923,   -0.836616576,   -0.240924537,\
     0.815585852,    0.346052110,    0.463751376,\
    -0.000029288,    0.000003709,  -36.585525513,\
   -29.723110199,    8.598756790,  -22.384565353,\
  -6227.334960938, 6300.517089844,  -20.000000000 )"
    
    #* CODE RUN
    cmd.set_view(singular_view_of_interest)
    cmd.hide("sticks", "resi 270+274")
    return
 
@cmd.extend
def pai_view_4():

    """
    View Angle Preset 4
    """
    
    singular_view_of_interest = "(\
    -0.304608017,   -0.424645096,    0.852577507,\
     0.491963923,   -0.836616576,   -0.240924537,\
     0.815585852,    0.346052110,    0.463751376,\
    -0.000029288,    0.000003709,  -52.795169830,\
   -29.723110199,    8.598756790,  -22.384565353,\
  -6211.127929688, 6316.724121094,  -20.000000000 )"
    
    #* CODE RUN
    cmd.set_view(singular_view_of_interest)
    cmd.hide("sticks", "resi 270+274")
    return
 
# * styles
@cmd.extend
def pai_style_1():

    Obj_whose_cartoon_you_want_to_Hide = "resi 266-291"

    cmd.hide("cartoon", Obj_whose_cartoon_you_want_to_Hide)
    cmd.remove("resn SOG")
    cmd.remove("elem H")

    set_color("cartoon", "white")
    util.cbaw("receptor")
    cmd.bg_color("white")
    return

@cmd.extend 
def pai_style_2():

    
    
    return
 
# * Residue show
@cmd.extend
def residue_style_all(representation, residues_of_interest):

    """Show side chain with main chain

        residues_of_interest : resi 168
    """

    cmd.show(f"{representation}",f"{residues_of_interest}")
    return

@cmd.extend
def residue_style_SC(representation, residues_of_interest):

    """Show side chain only

        residues_of_interest : resi 168
    """

    cmd.show(f"{representation}",f"((byres ({residues_of_interest}))&(sc.|(n. CA|n. N&r. PRO)))")
    return

# * ADN Specific Preset
@cmd.extend
def select_ADN_fingerprint():
    

    fp_resi = "resi 88+89+168+169+177+181+246+249+250+253+270+274+277+278"
    sw_resi = "resi 84+85"

    cmd.select("switch", f"{sw_resi}")
    cmd.select("fingerprint", f"{fp_resi}")
    print(f"(fingerprint): {fp_resi}")
    print(f"(switch): {sw_resi}")