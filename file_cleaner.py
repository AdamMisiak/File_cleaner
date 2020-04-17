import os
import shutil
from collections import Counter

def file_sorter():

    # CHANGE THE PATH YOU WANT TO SORT AND WHERE YOU WANT TO SAVE FOLDERS
    dir_to_sort = "C:\\Users\\USERNAME\\Desktop\\TEST\\all"
    dir_to_save = "C:\\Users\\USERNAME\\Desktop\\TEST"
    files_list = os.listdir(dir_to_sort)
    extension_list = []

    for file in files_list:
        extension = file.split('.')[-1]
        source = dir_to_sort + '\\\\' + str(file)
        extension_dir = dir_to_save + '\\\\' + extension

        # CREATING NEW FOLDERS FOR EXTENSIONS
        try:
            os.mkdir(extension_dir)
        except FileExistsError:
            pass

        # MOVING FILES TO PROPER FOLDERS
        shutil.move(source, extension_dir)
        extension_list.append(extension)

    # CREATING DICTIONARY OF EXTENSIONS
    counted_extensions_dict = Counter(extension_list)
    counted_extensions_dict_values = list(counted_extensions_dict.values())
    counted_extensions_dict_keys = list(counted_extensions_dict.keys())

    # PRINTING OUTPUTS
    print(f'Cleaning {dir_to_sort} done:')
    for index, element in enumerate(counted_extensions_dict):
        print(f'{counted_extensions_dict_values[index]} .{counted_extensions_dict_keys[index]} files sorted')
    if counted_extensions_dict == {}:
        print('No files to sort')
    else:
        print(f'All folders created in {dir_to_save}')

file_sorter()