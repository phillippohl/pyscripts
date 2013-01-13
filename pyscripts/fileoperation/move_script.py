'''
Created on 26.12.2012

@author: Phillipp
'''
import easygui,os,shutil,sys
from datetime import date

now = date.today()
SRC_PATH = r"C:\Users\Phillipp\Programing\workspace"
DST_PATH = r"E:\workspace"

def checksubdirectory(path):
    try:
        #print(os.listdir(path))
        return True
    except IOError as err:
        print(path + " has no subdirectories anymore!")
        return False

def copyworkspace(src, dst):
    for dir in os.listdir(src):
        src_dir = src + '\\' + dir
        dst_dir = dst + '\\' + dir

        if checksubdirectory(src_dir) == False:
            shutil.copy(src_dir, dst_dir)
        else:
            try:       
                if os.path.exists(src_dir) == False:   # test the existence of src_file
                    easygui.msgbox("Source directory: " + src_dir + " does not exist!")
                    sys.exit(0) 
                            
                if os.path.exists(dst_dir) == True:    # test the existence of dst_file
                    if easygui.ccbox(dst_dir + " already exists! Overwriting?", title):
                        #pass
                        print("Overwriting " + dst_dir)
                        shutil.rmtree(dst_dir)
                    else:
                        print("Not overwriting " + dst_dir)
                        continue

                if dir == ".metadata":
                    print("Directory: " + src + " skipped!")
                else:                  
                    shutil.copytree(src_dir, dst_dir) 
                    print("Directory: " + src + " successfully copied!")
            except IOError as err:
                easygui.msgbox("I/O error: {0}".format(err))
                        
    easygui.msgbox("Backup executed successfully!")

if now.strftime("%A") == "Tuesday" or now.strftime("%A") == "Friday":       
    msg = "Time to backup your eclipse workspace!\nDo you want to continue?\n\nSRC_PATH = " + SRC_PATH + "\nDST_PATH = " + DST_PATH 
    title = "Please Confirm"

    if easygui.ccbox(msg, title):
        copyworkspace(SRC_PATH, DST_PATH)
    else:
        sys.exit(0)