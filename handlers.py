def new_directory_name(home_dir):
  setting_new_directory = str(input(
    f'Informe um diretório: \n - personal-projects\n - course-projects\n - roleplay\nYour answer: '
  )
)

  if setting_new_directory == 'personal-projects':
    return f'{home_dir}/personal-projects'
  elif setting_new_directory == 'course-projects':
    return f'{home_dir}/course-projects'
  elif setting_new_directory == 'roleplay':
    return f'{home_dir}/roleplay'
  else:
    print('Valor inválido! Por favor, informe um diretório válido')