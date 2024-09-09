from fastapi_cli_command.cli.templates.base_template import BaseTemplate
from fastapi_cli_command.cli.templates.command_template import CommandTemplate
from fastapi_cli_command.cli.templates.controller_template import ControllerTemplate
from fastapi_cli_command.cli.templates.group_command_template import GroupCommandTemplate
from fastapi_cli_command.enums.module_enum import ModuleEnum


class TemplateFactory:
  @staticmethod
  def get_template(module_name: ModuleEnum, name: str) -> BaseTemplate:
    if module_name == ModuleEnum.COMMAND.value:
      return CommandTemplate(name)
    if module_name == ModuleEnum.GROUP_COMMAND.value:
      return GroupCommandTemplate(name)
    if module_name == ModuleEnum.CONTROLLER.value:
      return ControllerTemplate(name)
    else:
      raise ValueError(f'Not support module {module_name} yet.')
