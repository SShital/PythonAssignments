# delete empty files in a dir
import os.path as opath
import os


def delete_empty(file_path):

    if opath.isdir(file_path):
        for root, dirs, files in os.walk(file_path):
            for file_names in files:
                # print os.stat(file_names).st_size, " ", file_names
                if opath.exists(file_names):
                    if opath.getsize(file_names) == 0:
                        os.remove(file_path+file_names)
    else:
        print("File does not exists.")


dir_name = raw_input("Enter a directory path:")
delete_empty(dir_name)


def archive_directory(output_dir, dir_name):
    import shutil
    shutil.make_archive(output_dir+"ziped_it", "zip", dir_name)


archive_directory("D:/", "D:/python assingments/study material"
                         "/day4_assignments/")
