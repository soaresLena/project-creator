from pathlib import Path
import os
from bash_commands import update_linux, install_pip, install_venv, create_venv, activate_venv, open_project

home_directory = Path.home()
os.chdir(home_directory)

def divider():
  global div
  div = '='*50
  print(div)

setting_new_directory = str(input(
  f'Informe um diretório: {divider}\n - personal-projects\n - course-projects\n - roleplay\nYour answer: '
  )
)

if setting_new_directory == 'personal-projects':
  f'{home_directory}/personal-projects'
elif setting_new_directory == 'course-projects':
  f'{home_directory}/course-projects'
elif setting_new_directory == 'roleplay':
  f'{home_directory}/roleplay'
else:
  print('Valor inválido! Por favor, informe um diretório válido')
  
default_directory = f'{home_directory}/{setting_new_directory}'

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

update_linux()
install_pip()
install_venv()
create_venv()
activate_venv()
open_project(complete_project_path)