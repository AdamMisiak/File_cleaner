import os
import shutil

def file_sorter():
    txt_counter, pdf_counter, exe_counter, not_moved = 0, 0, 0, 0

    # ADD HERE PATH TO CATALOG YOU WANT TO SORT
    dir_to_sort = "C:\\Users\\adamm\\Desktop\\TEST\\all"
    main_dir = "C:\\Users\\adamm\\Desktop\\TEST"
    files_list = os.listdir(dir_to_sort)


    for file in files_list:
        extension = file.split('.')[-1]
        source = dir_to_sort + '\\\\' + str(file)
        extension_dir = main_dir + '\\\\' + extension
        try:
            os.mkdir(extension_dir)
        except FileExistsError:
            pass

        shutil.move(source, extension_dir)
zrob liste dodajaca ext i potem zliczanie ilosci


        # if extension == "txt":
        #     shutil.move(source, txt_destination)
        #     txt_counter += 1
        # elif extension == "pdf":
        #     shutil.move(source, pdf_destination)
        #     pdf_counter += 1
        # elif extension == "exe":
        #     shutil.move(source, exe_destination)
        #     exe_counter += 1
        # # ADD HERE MORE ELIFS FOR NEW EXTENSIONS OF FILES
        # else:
        #     not_moved += 1

    # print(f"Sorting done: \n {txt_counter} txt files sorted \n {pdf_counter} pdf files sorted \n" \
    #       f" {exe_counter} exe files sorted \n {not_moved} files not sorted")



file_sorter()