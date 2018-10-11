import os

def listdir_nohidden(path_to_folder, startswith=False, folders_only = False):
    if startswith:
        list_of_nonhidden_files_folders = [f for f in os.listdir(path_to_folder) if f.startswith(startswith) ]
    else :
        list_of_nonhidden_files_folders = [f for f in os.listdir(path_to_folder) if not(f.startswith('.') or f.startswith('Desk')) ]
    if folders_only:
        folders_only = [ name for name in list_of_nonhidden_files_folders if os.path.isdir(os.path.join(path_to_folder, name)) ]
        folders_only.sort()
        return folders_only
    else: 
        list_of_nonhidden_files_folders.sort()
        return list_of_nonhidden_files_folders

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
