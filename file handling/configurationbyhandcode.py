import os

def delete_dir(name: str):
    target = name
    os.rmdir(target)

def delete_file(name: str):
    target = name
    os.remove(target)
    

def get_name_DeleteFile():
    name = input("Enter the file name you want to delete permanently: ")
    name = str(name)
    print("Your selected file name : "+ name)
    return name

def get_name_DeleteDir():
    name = input("Enter the Directory name you want to delete permanently: ")
    name = str(name)
    print("Your selected Directory name : "+ name)
    return name

def user_choice():

    choice = int(input("Do you want to delete the file or directory : 0 (no) or 1 (yes): "))
    if choice == 1:
        tar = input("Select the file or select the directory :  ")

        if tar == "FILE" or tar == "file" or tar == "File":
            target = get_name_DeleteFile()

            if os.path.exists(target):
                delete_file(target)
            else:
                print("Warning!  You are giving wrong file name to delete.....")

        else:
            target = get_name_DeleteDir()

            if os.path.exists(target):
                delete_dir(target)
            else:
                print("Warning!  You are giving wrong Directory name to delete.....")

    if choice == 0:
        return
    
    if choice != 0 and choice != 1:
        print("Your giving wrong input to run the program..")
    
user_choice()




