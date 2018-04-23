import os
def rename_files():

    file_list = os.listdir(r"C:\Python27\learning\changing file names\scramble practice")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)
    os.chdir(r"C:\Python27\learning\changing file names\scramble practice")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))

rename_files()
