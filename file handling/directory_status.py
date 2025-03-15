import os

location = os.getcwd()  # Get current working directory
print("Your current location:", location)

os.chdir("../")  # Change to the parent directory

new_location = os.getcwd()  # Get the updated location
print("New location after changing directory:", new_location)
