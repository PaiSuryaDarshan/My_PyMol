from pymol import cmd

@cmd.extend
def hello_world(name="!"):
    print(f"Hello, {name}")
    return

@cmd.extend
def create(name, selection, source_state=0,
           target_state=0, discrete=0, zoom=-1, quiet=1,
           singletons=0, extract=None):
    cmd.create(name, selection, source_state,
           target_state)
    return

print("PyMol_God.py imported successfully.")