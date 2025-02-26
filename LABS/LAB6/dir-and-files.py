import os

#1 Write a Python program to list only directories, files and all directories, files in a specified path.
path = r"F:\VsCodeProjects\PP2\LABS\LAB6\testfiles\1"
file_path1 = r"F:\VsCodeProjects\PP2\LABS\LAB6\testfiles\1\1.1.txt"
file_path2 = r"F:\VsCodeProjects\PP2\LABS\LAB6\testfiles\1\1.2.txt"
file_path3 = r"F:\VsCodeProjects\PP2\LABS\LAB6\testfiles\1\1.3.txt"
folder_path = r"F:\VsCodeProjects\PP2\LABS\LAB6\testfiles\1\folder"
'''
if os.path.exists(path):
    choice = input("What exactly do you want to see? ")
    if choice == "DF" or choice == "df":
        for root, dirs, files in os.walk(path):
            print(f'Current Directory: {root}\nSubdirectories: {dirs}\nFiles: {files}\n'+'-'*25)
    elif choice == "OD" or choice == "od":
        for root, dirs, files in os.walk(path):
            print(f'Current Directory: {root}\nSubdirectories: {dirs}\n'+'-'*25)
else:
    print(f"The path '{path}' does not exist.")
'''
#2 Write a Python program to check for access to a specified path. 
#  Test the existence, readability, writability and executability of the specified path
'''
if os.path.exists(path):
    print(f"The path '{path}' exists.")
    print(f"The path '{path}' is readable.") if os.access(path, os.R_OK) else print(f"The path '{path}' is not readable.")
    print(f"The path '{path}' is writable.") if os.access(path, os.W_OK) else print(f"The path '{path}' is not writable.")
    print(f"The path '{path}' is executable.") if os.access(path, os.X_OK) else print(f"The path '{path}' is not executable.")
else:
    print(f"The path '{path}' does not exist.")
'''
#3 Write a Python program to test whether a given path exists or not. 
#  If the path exists find the filename and directory portion of the given path.
'''
def isfile(path):
    if os.path.isdir(path):
        return f"Directory: '{path}'"
    elif os.path.isfile(path):
        return f"File: '{path}'"
    else:
        return f"The path '{path}' does not exist."

if os.path.exists(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        print(isfile(full_path))
else:
    print(f"The path '{path}' does not exist.")
'''

#4 Write a Python program to count the number of lines in a text file.
'''
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return f"The file '{file_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

print(f"The number of lines in the file is: {count_lines_in_file(file_path)}")
'''

#5 Write a Python program to write a list to a file.
'''
text_to_append = ["Hello", "World", "How", "Are", "You"]
try:
    if os.path.isfile(file_path1):
        with open(file_path1, 'a') as file:
            for i in text_to_append:
                file.write(i + '\n')
except FileNotFoundError:
    print(FileNotFoundError)
except Exception as e:
    print(f"An error occurred: {e}")
'''

#6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
'''
def createfiles():
    try:
        for i in range(26):
            file = open(f"testfiles/folder/{chr(65+i)}.txt", 'w')
            file.write(f"Hello, this is the content of the new file.\n{chr(65+i)}")
    except Exception as e:
        print(f"An error occurred: {e}")
def deletefiles():
    try:
        for i in range(26):
            os.remove(f"testfiles/folder/{chr(65+i)}.txt")
    except Exception as e:
        print(f"An error occurred: {e}")  
'''

#7 Write a Python program to copy the contents of a file to another file
'''
def read_file(file_path):
    try:
        if os.path.isfile(file_path2) and os.path.isfile(file_path3):
            txt_list = []
            with open(file_path2, 'r') as file2:
                for line in file2:
                    txt_list.append(line.strip())
            with open(file_path3, 'w') as file3:
                for i in txt_list:
                    file3.write(f"{i}\n")
        else:
            print(f"The file '{file_path}' does not exist.")
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

read_file(file_path1)
'''

#8 Write a Python program to delete file by specified path. 
#  Before deleting check for access and whether a given path exists or not.
def deletefiles():
    try:
        if os.path.isfile(file_path2):
            os.remove(file_path2)
    except Exception as e:
        print(f"An error occurred: {e}")  
deletefiles()