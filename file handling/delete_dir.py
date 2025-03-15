import os

def delete_dir(name: str):
    target = name
    os.rmdir(target)


del_dir = ["a", "b", "v"]

for t in del_dir:
    delete_dir(t)