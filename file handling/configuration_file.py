def create_file(file_name: str):
    """Creates a new file if it does not exist."""
    try:
        file = open(file_name, "x")
        file.close()
        print(f"✅ Your file '{file_name}' has been created successfully!")
    except FileExistsError:
        print(f"⚠️ Error: The file '{file_name}' already exists.")

def adding_text(file_name: str, content: str):
    """Appends text to an existing file."""
    try:
        with open(file_name, "a") as file:
            file.write(content + "\n")
        print(f"✅ Text added successfully to '{file_name}'.")
    except FileNotFoundError:
        print(f"⚠️ Error: The file '{file_name}' does not exist.")

def read_file(file_name: str):
    """Reads the content of a file."""
    try:
        with open(file_name, "r") as file:
            content = file.read()
        print(f"\n📖 Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"⚠️ Error: The file '{file_name}' does not exist.")

def input_function():
    """Runs a loop that allows users to repeatedly choose an action."""
    while True:
        print("\n🔹 Available choices: create | write | read | exit")
        choice = input("Enter your choice: ").strip().lower()

        if choice == "create":
            file_name = input("Enter the file name: ").strip()
            create_file(file_name)

        elif choice == "write":
            file_name = input("Enter the file name: ").strip()
            content = input("Enter the text you want to add: ").strip()
            adding_text(file_name, content)

        elif choice == "read":
            file_name = input("Enter the file name: ").strip()
            read_file(file_name)

        elif choice == "exit":
            print("👋 Exiting the program. Have a great day!")
            break

        else:
            print("⚠️ Invalid choice! Please enter 'create', 'write', 'read', or 'exit'.")

input_function()
