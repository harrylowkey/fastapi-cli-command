import importlib

from fastapi_cli_command.helpers import ModuleHelper


class FastAPICli:
  @staticmethod
  def config(module_paths: list[str], command_modules: list[str]):
    ModuleHelper(module_paths).load_modules()

    FastAPICli.load_commands(command_modules)

  @staticmethod
  def load_commands(module_paths: list[str]):
    for path in module_paths:
      importlib.import_module(path)
