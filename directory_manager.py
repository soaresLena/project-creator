from pathlib import Path
import os

def change_dir(dir:str):
  return os.chdir(dir)

def change_home_directory():
  home_directory = Path.home()
  change_dir(home_directory)
  return home_directory
  
def make_dir(dir:str):
  if os.path.exists(dir) == False:
    os.mkdir(dir)

def check_directory_exists(dir:str):
  make_dir(dir)
  
  return change_dir(dir)
  
def check_file_exists(complete_project_path, file:str):
  if os.path.isfile(f'{complete_project_path}/{file}') == False:
    return os.mknod(file)