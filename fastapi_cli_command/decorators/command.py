import asyncio

import click

from fastapi_cli_command.helpers import parse_params, resolve_dependencies
from fastapi_cli_command.storage import CLI_COMMANDS


def command(name: str, **kwargs):
  def decorator(cls):
    if not 'run' in cls.__dict__:
      raise Exception(f'Command must implement the run method.')

    method = getattr(cls, 'run')
    params = parse_params(method)

    async def command(*args, **kwargs):
      dependencies = await resolve_dependencies(cls.__init__)

      instance = cls(**dependencies)
      command = getattr(instance, 'run')

      if asyncio.iscoroutinefunction(command):
        return await command(*args, **kwargs)

      return command(*args, **kwargs)

    CLI_COMMANDS[name] = click.Command(
      name=method.__name__, callback=command, params=params, help=kwargs.get('help', None)
    )

  return decorator
