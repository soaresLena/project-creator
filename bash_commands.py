import subprocess

def update_linux():
  return subprocess.run(
    'sudo apt update -y && sudo apt-get upgrade -y', 
    shell=True, 
    check=True, 
    executable='/bin/bash'
  )

def install_pip():
  return subprocess.run(
    'sudo apt install python3-pip', 
    shell=True, 
    check=True, 
    executable='/bin/bash'
  )
  
def install_venv():
  return subprocess.run(
    'sudo apt install python3-venv', 
    shell=True, 
    check=True, 
    executable='/bin/bash'
  )
  
def create_venv():
  return subprocess.run(
    'python3 -m venv .venv', 
    shell=True, 
    check=True, 
    executable='/bin/bash'
  )
  
def activate_venv():
  return subprocess.run(
    'source .venv/bin/activate', 
    shell=True, 
    check=True, 
    executable='/bin/bash'
  )
  
def open_project(complete_project_path):
  return subprocess.run(
    f'code {complete_project_path}', 
    shell=True, 
    check=True, 
    executable='/bin/bash'
  )
