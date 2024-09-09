import logging
import sys

from click import Command, Group

from fastapi_cli_command.bases.cli import BaseCLI
from fastapi_cli_command.fastapi_cli import FastAPICli
from fastapi_cli_command.storage import CLI_COMMAND_GROUPS, CLI_COMMANDS

logging.warning('Start run command')

# FIXME: module paths should be configurable in client codes
FastAPICli.config(
  module_paths=['*/*/entities/*.py', '*/*/commands/*.py'],
  command_modules=['fastapi_cli_command.cli.commands.generate_command'],
)


class CLI(BaseCLI):
  def __init__(self, command_name: str):
    self._command_name = command_name

  def run(self):
    command = CLI_COMMANDS.get(self._command_name)
    if command:
      return self._run_command(command)

    return self._run_group()

  def _run_command(self, command: Command):
    if not command.callback:
      raise Exception(f'Command {command.name} is not found.')

    self._check_async_function([command])

    return command.main(args=sys.argv[2:])

  def _run_group(self):
    cli_app = Group('main')

    for _, group_cls in CLI_COMMAND_GROUPS.items():
      cli_group: Group = getattr(group_cls, '_cli_group')
      self._check_async_function(cli_group.commands.values())
      cli_app.add_command(cli_group)

    return cli_app.main(args=sys.argv[1:])


command = sys.argv[1] if len(sys.argv) > 1 else None
if not command:
  raise ValueError('No command provided.')

cli = CLI(command).run

if __name__ == '__main__':
  cli()
