from pathlib import Path
import os
import subprocess

home_directory = Path.home()
os.chdir(home_directory)

default_directory = f'{home_directory}/tests'

if os.path.exists(default_directory) == False:
  os.mkdir(default_directory)

os.chdir(default_directory)

project_name = str(input('Infome o nome do projeto: '))

complete_project_path = f'{default_directory}/{project_name}'

if os.path.exists(complete_project_path) == False:
  os.mkdir(complete_project_path)
  
os.chdir(complete_project_path)

if os.path.isfile(f'{complete_project_path}/main.py') == False:
  os.mknod('main.py')
  
subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''sudo apt install python3-venv''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''python3 -m venv .venv''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')
subprocess.run(f'''code {complete_project_path}''', shell=True, check=True, executable='/bin/bash')