from click import Option
from fastapi import Depends

from fastapi_cli_command.cli.generators import Generator
from fastapi_cli_command.decorators import cli_command, cli_command_group


class GeneratorOptions:
  NAME = Option(
    ['--name'],
    help='Name of the option paramter',
    required=True,
    prompt=True,
    type=str,
  )
  PATH = Option(['--path'], help='Path to the command location', type=str, required=True)


@cli_command_group('generate')
class GeneratorGroupCommand:
  def __init__(self, generator: Generator = Depends()):
    self.generator = generator

  @cli_command('command')
  def generate_command(self, name: GeneratorOptions.NAME, path: GeneratorOptions.PATH):
    return self.generator.generate_command(name, path)

  @cli_command('group-command')
  def generate_group_command(self, name: GeneratorOptions.NAME, path: GeneratorOptions.PATH):
    return self.generator.generate_group_command(name, path)
