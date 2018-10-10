import os
def listdir_nohidden(path_to_folder):
    list_of_files = []
    for f in os.listdir(path_to_folder):
        if f.startswith('P'):
            list_of_files.append(f)
    list_of_files.sort()
    return list_of_files
