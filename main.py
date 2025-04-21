from directory_manager import capture_home_directory, check_directory_exists, check_file_exists, change_dir
from bash_commands import update_linux, install_pip, install_venv, create_venv, activate_venv, open_project

home_dir = capture_home_directory()
change_dir(home_dir)

setting_new_directory = str(input(
  f'Informe um diretório: \n - personal-projects\n - course-projects\n - roleplay\nYour answer: '
  )
)

if setting_new_directory == 'personal-projects':
  f'{home_dir}/personal-projects'
elif setting_new_directory == 'course-projects':
  f'{home_dir}/course-projects'
elif setting_new_directory == 'roleplay':
  f'{home_dir}/roleplay'
else:
  print('Valor inválido! Por favor, informe um diretório válido')
  
default_directory = f'{home_dir}/{setting_new_directory}'
check_directory_exists(default_directory)
project_name = str(input('Infome o nome do projeto: '))
complete_project_path = f'{default_directory}/{project_name}'
check_directory_exists(complete_project_path)
check_file_exists(complete_project_path, 'main.py')

update_linux()
install_pip()
install_venv()
create_venv()
activate_venv()
open_project(complete_project_path)