import os

def listdir_nohidden(path_to_folder, startswith=False):
    list_of_files = []
    if startswith:
        for f in os.listdir(path_to_folder):
            if f.startswith(startswith):
                list_of_files.append(f)
        list_of_files.sort()
    else :
        for f in os.listdir(path_to_folder):
            if not f.startswith('.'):
                list_of_files.append(f)
    return list_of_files

