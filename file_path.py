import os 
file_path=input("Enter the file path: ")
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")