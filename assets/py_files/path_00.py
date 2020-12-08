from pathlib import Path
import os

folder_name = input('Folder name: ')

def create_dir(folder_name):
  Path(folder_name).mkdir(parents=True, exist_ok=True) # create a dir
  os.chdir(Path(folder_name)) # change dir
  os.chdir(Path.cwd().parent) # return to parent dir

create_dir(folder_name)