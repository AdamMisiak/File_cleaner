import os
import shutil
from collections import Counter

def file_sorter():

    # ADD HERE PATH TO CATALOG YOU WANT TO SORT
    dir_to_sort = "C:\\Users\\adamm\\Desktop\\TEST\\all"
    main_dir = "C:\\Users\\adamm\\Desktop\\TEST"
    files_list = os.listdir(dir_to_sort)
    extension_list = []

    for file in files_list:
        extension = file.split('.')[-1]
        source = dir_to_sort + '\\\\' + str(file)
        extension_dir = main_dir + '\\\\' + extension

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
    len_of_dict = len(counted_extensions_dict)

    # PRINTING OUTPUTS
    print(f'Cleaning {dir_to_sort} done:')
    for index, element in enumerate(counted_extensions_dict):
        print(f'{counted_extensions_dict_values[index]} {counted_extensions_dict_keys[index]} extensions sorted')
    if counted_extensions_dict == {}:
        print('No files to sort')
    else:
        print(f'All folders created in {main_dir}')





file_sorter()