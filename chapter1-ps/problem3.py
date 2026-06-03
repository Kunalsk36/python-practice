# This script lists the contents of the root directory and identifies whether each item is a file or a directory.

# importing the os module to interact with the operating system
import os

# specifying the directory path to list its contents
directory_path = "/"

# using the os.listdir() function to get a list of items in the directory
contents = os.listdir(directory_path)

# iterating through the list of items and checking if each item is a file or a directory
for item in contents:
    item_path = os.path.join(directory_path, item)
    item_type = "directory" if os.path.isdir(item_path) else "file"
    print(f"{item} is a {item_type}.")