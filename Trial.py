 # * Test Script

#* 1. Retrieving the PDB file ###

# Close / Erase code

fetch 1j95, Kchannel, async=0  

#* 2. Establishing Selections and Objects ###

create SFilter, resi 75-80

select K, name K

deselect

#* 3. Visualisation ###

remove resn TBA # Solvent used for/during crystallisation

util.cbc

as sticks, Sfilter 
color white, SFilter
util.cbaw Sfilter
util.cbaw K

#* 3. Orientation ###

get_view
# copy-paste

#* 4. Save Scene ###

scene F1, store

#* 5. New Scene ###
hide sticks, SFilter
create Kcomplex, resi 77+78+201
as sticks, Kcomplex
util.cbaw Kcomplex
hide sphere, resi 202-204

get_view
# copy-paste

scene F2, store

#* 6. Publication Final Touch ###
bg_color white 

#* 7. Save
save /Users/pai.suryadarshan/Desktop/Academics/Year_3/ChemDisease_and_Therapy/My_PyMol/Trial.pse