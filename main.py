from directory_manager import change_home_directory, check_directory_exists, check_file_exists
from handlers import new_directory_name
from bash_commands import update_linux, install_pip, install_venv, create_venv, activate_venv, open_project

home_dir = change_home_directory()
setting_new_directory = new_directory_name(home_dir)
check_directory_exists(setting_new_directory)
project_name = str(input('Infome o nome do projeto: '))
complete_project_path = f'{setting_new_directory}/{project_name}'
check_directory_exists(complete_project_path)
check_file_exists(complete_project_path, 'main.py')

update_linux()
install_pip()
install_venv()
create_venv()
activate_venv()
open_project(complete_project_path)