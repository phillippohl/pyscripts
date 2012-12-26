'''
Created on 26.12.2012

@author: Phillipp
'''
import easygui,os,time

def get_input():
    dir_path = easygui.diropenbox("Choose directory")
    
    new_file_name = easygui.enterbox("Please enter the new name convention for the files' naming.", "Name convention")
    if new_file_name == None:
        sys.exit(0)
    if new_file_name == "":
        while(new_file_name == ""):
            easygui.msgbox("You did not specified a name convention for the files' naming. Please do so!", "Attention!")
            new_file_name = easygui.enterbox("Please enter the new name convention for the files' naming.", "Name convention")
        
    numeration_type = easygui.choicebox("What kind of numeration do you prefer?", "Numeration type", ["Increasing numbers", "Creation date", "Modification date"])
    if numeration_type == None:
        sys.exit(0)
    else:
        print("Selected numeration type: " + numeration_type)
        rename_files(dir_path, new_file_name, numeration_type)
    
def rename_files(dir_path, new_file_name, numeration_type):
    counter = 0
    print("Initial files within path:\n" + "  > " + dir_path + "\n")
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

    print("\nRenamed files within path:\n" + "  > " + dir_path + "\n")
    for file in os.listdir(dir_path):
        print(file)

if easygui.ccbox("You have executed the renaming script.\nDo you want to continue?", "Please Confirm"):
    get_input()
else:
    sys.exit(0)
