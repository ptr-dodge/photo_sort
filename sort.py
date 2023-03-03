import os
import time
import sys
import shutil


def sort_files(directory):
    # get list of files
    files = os.listdir(os.path.abspath(directory))

    for filename in files:

        file_full_path = os.path.join(directory, filename)

        date_modified = os.path.getmtime(file_full_path)
        month = time.ctime(date_modified)[4:7]
        path_to_move_to = os.path.split(
            directory)[0] + "/" + month + "_" + time.ctime(date_modified)[20:26]

        if not os.path.exists(path_to_move_to):
            os.mkdir(path_to_move_to)

        # handle duplicate files
        if os.path.exists(path_to_move_to+"/"+filename):

            # if remove flags are set, remove file if duplicate
            if "--remove" or "-r" in sys.argv:
                os.remove(file_full_path)
                break
            else:
                # if remove flags are not set, tack on "_1" to the file name

                # get the file name and extension
                base, extension = os.path.splitext(filename)
                # rename the file and move it
                shutil.move(file_full_path, path_to_move_to +
                            "/"+base+"_1"+extension)
        else:
            # if there is no duplicate, move the file
            shutil.move(file_full_path, path_to_move_to+"/"+filename)


dir_list = sys.argv
if "-r" in sys.argv:
    dir_list.remove("-r")
elif "--remove" in sys.argv:
    dir_list.remove("--remove")


dir_list.pop(0)
for directory in dir_list:

    print(f"sorted for directory \"{ directory }\"")
    sort_files(directory)
