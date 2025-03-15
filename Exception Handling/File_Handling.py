def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
        print(f"\n📖 Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"⚠️ Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

file_name = input("Enter the file name to read: ").strip()
read_file(file_name)
