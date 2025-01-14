 # * Default Script

#* 1. Retrieving the PDB file

# Close / Erase code

# fetch PDB
fetch {{PDB ID}}, {{Name_for_Object}}, async=0  # aysnc=0 -> Prevents any code beneath from 
                                                # running till this one is completed

#* 2. Establishing Selections and Objects

# Create Object called select filter, selecting residues from A to B 
create SFilter, resi {{A-B}}

# Name Selection WITHOUT creating a new object
select {{residues/ion}}, name {{name_of_choice_for_selection}}

deselect

#* 3. Visualisation

# Removing Residues or molecules (Useful to remove solvents like water)
remove resn {{solvent_name}}  # water --> HOH

# Utility.ColorByChain
util.cbc

# This is where we reap the advantages of using 
# create a filter rather than select and name Sfilter (See Theory 1.1)
as sticks, Sfilter 

# ----------- PyMol Theory 1.1 -----------

# "show" --> Something like 'show sticks' Overlays current representation

# "as" --> Something like 'as sticks' REPLACES strictly 
#          the selected region of current representation
#          With the desired representation 

# Creating objects are really good as it allows your main chains 
# and side chains to be visualised differently. 
# For example, the main chain can be coloured by chain ID, 
# whereas the side chains of interest can be coloured 
# using the desired colour to emphasise them.

# CAVEAT: Using as is only possible, if you have defined 
# the selection as an object and not just a selection 

# ! WARNING: Any Attempt to using "as" for a 
# ! "named selection" rather than an object will  
# ! create holes in your current visualisation!

# Here we used "create SFilter, resi {{A-B}}"" 
# and NOT "select resi {{A-B}}, name {{SFilter}}" 

# ----------- PyMol Theory 1.1 -----------


# Change color of Object
color white, SFilter

# Utility.ColorByAtom_White 
util.cbaw Sfilter
util.cbaw {{ion}} # Uses the Correct colour code associated with the ion.

# ----------- PyMol Theory 1.2 -----------

# Utility.ColorByAtomWhite --> 'White' at the end tells that 
#                 the Carbon atoms should be colored White

# ----------- PyMol Theory 1.2 -----------

#* 3. Orientation

# Step 1: Adjust molecule to desired view
# Step 2: You get view to obtain the coordinates


# Step 3:Copy paste the coordinates and save it to a variable

