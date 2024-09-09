from fastapi_cli_command.cli.templates import TemplateFactory
from fastapi_cli_command.enums.module_enum import ModuleEnum
from fastapi_cli_command.helpers import snake_key


class Generator:
  def __init__(self):
    self.template_factory = TemplateFactory()

  def get_template_file_path(self, path: str, module_name: ModuleEnum, name: str):
    defix = ''

    if module_name in [ModuleEnum.COMMAND.value, ModuleEnum.GROUP_COMMAND.value]:
      defix = '_command'
    if module_name == ModuleEnum.CONTROLLER.value:
      defix = '_controller'

    return snake_key(f'{path}/{name}{defix}.py')

  def generate(self, module_name: ModuleEnum, name: str, path: str):
    template = self.template_factory.get_template(module_name, name)
    template_file_path = self.get_template_file_path(path, module_name, name)

    with open(template_file_path, 'w') as f:
      f.write(template.generate_template())

  def generate_command(self, name: str, path: str):
    """
    Create a new command

    :param name: The name of the command

    The files structure are:
    .
    ├── ...
    └── src/
      └── module_name/
        └── commands/
          └── {command_name}_command.py
    """
    self.generate(ModuleEnum.COMMAND, name, path)

  def generate_group_command(self, name: str, path: str):
    """
    Create a new group command

    :param name: The name of the command

    The files structure are:
    .
    ├── ...
    └── src/
      └── module_name/
        └── commands/
          └── {command_name}_command.py
    """
    self.generate(ModuleEnum.GROUP_COMMAND, name, path)
