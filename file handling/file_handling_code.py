def create_file(file_name: str):
    name = file_name
    file = open(name, "x")
    file.close()
    print(f"Your file {name} has been created successfully....")

def adding_text(file_name: str, content: str):
    name = file_name
    file = open(name, "a")
    file.write(content)
    file.close()
    print(f"You have added succesfully in the {name} file")

def read_file(file_name: str):
    name = file_name
    file = open(name, "r")
    con = file.read()
    print("Content:\t" + con)
    file.close()

def input_function():

    while True:
        ch = input("Enter your choice : read,write,create choose one: ")
        ch = str(ch)
        ch = ch.lower()
        if ch == "create":
            name = input("Enter the file name : ")
            name = str(name)
            create_file(name)
            print("Create  Operation Successfull....")

        elif ch == "write":
            name = str(input("Enter the file name : "))
            con = str(input("ENter the text you want to add in the file : "))
            adding_text(name, con)
            print("Your adding function run finely....")

        elif ch == "read":
            name = input("Enter the file name : ")
            name = str(name)
            read_file(name)
            print("Read Operation Successfull....")

        elif ch == "exit":
            print("You are good bye tata.....")
            break

input_function()