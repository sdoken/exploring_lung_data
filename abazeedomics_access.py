import os

def listdir_nohidden_two(path_to_folder, startswith=False):
    if startswith:
        list_of_files = [f for f in os.listdir(path_to_folder) if f.startswith(startswith) ]
    else :
        list_of_files = [f for f in os.listdir(path_to_folder) if not(f.startswith('.') or 
                                                                    f.startswith('Desk'))]
    list_of_files.sort()
    return list_of_files

'''
def listdir_nohidden(path_to_folder, startswith=False):
    list_of_files = []
    if startswith:
        for f in os.listdir(path_to_folder):
            if f.startswith(startswith):
                list_of_files.append(f)
        list_of_files.sort()
        return list_of_files
    else :
        for f in os.listdir(path_to_folder):
            if not (f.startswith('.') or f.startswith('Desk') ):
                list_of_files.append(f)
        list_of_files.sort()
        return list_of_files
'''
