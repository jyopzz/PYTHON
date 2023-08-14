import pandas#external modules
import os#inbuild modules
one=pandas.read_csv("Jyothis.csv")
print(one)

currentdir=os.getcwd()
print("Current working directories: ",currentdir)

directory = r"C:\Users\jyoth\OneDrive\Documents\PYTHON" #or "C:/Users/jyoth/OneDrive/Documents"
files_and_dirs = os.listdir(directory)
print("Files and Directories in ", directory, ":", files_and_dirs)
