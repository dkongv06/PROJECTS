import os
def rename_files():
    #(step1) get file names from a folder
    #os.listdir() will get you everything thats in a directory
    #os is a module, listdir() is a fucntion
    
    file_list = os.listdir(r"C:\Python27\learning\changing file names\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"C:\Python27\learning\changing file names\prank")

    #r means raw path, tells Python not to interpret path as anything else
    #file_list is called a variable

    #(step2) for each file, rename filename to get rid of just numbers included in the name of the files
    #after google search, which is what programmers do if desired action already exists, i found the function rename(src,dst)
    #os.rename(), os is the module, rename() is the function, src is the source of the current file, dst is the destination
    #rename(src,dst) takes in the source of the current name of the file and changes it to the destination or the new name of the file we want it to be
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))

    #this code says for each photo in file_list, which we defined as a module with a function to retrieve files from a folder, perform this action "os.rename()"
    #file_name is the old file name, file_name.translate() is the new name that is produced by the function
rename_files()


