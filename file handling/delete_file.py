import os

def delete_file(name: str):
    target = name
    os.remove(target)
    


del_dir = ["a", "b", "v"]

for t in del_dir:
    delete_file(t)