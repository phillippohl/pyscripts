'''
Created on 26.12.2012

@author: Phillipp
'''
import easygui,os,sys,time

DEFAULT_DIRECTORY = r"E:\Dropbox\Daten\Programmieren\testspace"

def get_input():
    dir_path = get_dir()
    new_file_name = set_file()
    numeration_type = set_num()
    rename_files(dir_path, new_file_name, numeration_type)
    
def get_dir():
    dir_path = None
    while(dir_path == None):
        dir_path = easygui.diropenbox(msg="Choose directory",title="Choose directory",default=DEFAULT_DIRECTORY)
        if dir_path == None:
            if easygui.ccbox("Are you sure that you want to stop the scrip's execution?", "Please confirm"):
                sys.exit(0)
            else:
                continue
    print("Chosen directory: %s" % dir_path)
    return dir_path

def set_file():
    file_name = None
    while(file_name == None):
        file_name = easygui.enterbox("Please enter the new name convention for the files' naming.", "Name convention")
        if file_name == None:
            if easygui.ccbox("Are you sure that you want to stop the scrip's execution?", "Please confirm"):
                sys.exit(0)
            else:
                continue
        if file_name == "":
            easygui.msgbox("You did not specified a name convention for the files' naming. Please do so!", "Attention!")
            file_name = None
    print("Chosen name convention: %s" % file_name)
    return file_name

def set_num():
    numeration_type = None
    while(numeration_type == None):
        numeration_type = easygui.choicebox("What kind of numeration do you prefer?", "Numeration type", ["Increasing numbers", "Creation date", "Modification date"])
        if numeration_type == None:
            if easygui.ccbox("Are you sure that you want to stop the scrip's execution?", "Please confirm"):
                sys.exit(0)
            else:
                continue
        else:
            print("Chosen numeration type: %s" % numeration_type)
            return numeration_type

def rename_files(dir_path, new_file_name, numeration_type):
    counter = 0
    print("Initial files within directory:")
    for file in os.listdir(dir_path):
        print(file)
        
        split_helper = file.split(".")
        file_type = split_helper[1]
        
        src_file = dir_path + "\\" + file
        dst_file = dir_path + "\\" + new_file_name

        if numeration_type == "Increasing numbers":
            counter += 1
            dst_file += str(counter) + "." + file_type
            
        elif numeration_type == "Creation date":
            time_helper = time.ctime(os.path.getctime(src_file))
            time_helper = time.strftime("%Y %m %d %M %S")
            time_helper = time_helper.replace(" ", "_")
            dst_file += time_helper + "." + file_type

        elif numeration_type == "Modification date":
            time_helper = time.ctime(os.path.getmtime(src_file)) + "." + file_type
            time_helper = time.strftime("%Y%M%d")
            time_helper = time_helper.replace(" ", "_")
            dst_file += time_helper + "." + file_type
            while(os.path.exists(dst_file) == True):
                i = 1
                dst_file += "_" + str(i)
        else:
            print("Wrong or unsupported numeration type!")
            sys.exit(0)
        
        os.rename(src_file, dst_file)

    print("Renamed files within directory:")
    for file in os.listdir(dir_path):
        print(file)
        
def on_start():
    print("##############################\n### Welcome to move_script!###\n##############################\n")
    if easygui.ccbox("You have executed the renaming script.\nDo you want to continue?", "Please confirm"):
        get_input()
    else:
        sys.exit(0)

on_start()