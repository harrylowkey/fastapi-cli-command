import asyncio

import click

from fastapi_cli_command.helpers import parse_params, resolve_dependencies
from fastapi_cli_command.storage import CLI_COMMAND_GROUPS


def cli_command_group(name: str, **kwargs):
  def decorator(cls):
    cli_group = click.Group(name, **kwargs)
    setattr(cls, '_cli_group', cli_group)

    CLI_COMMAND_GROUPS[name] = cls

    for method_name, method in cls.__dict__.items():
      if callable(method) and hasattr(method, '_cli_command'):
        params = parse_params(method)

        # we need to create the wrapper to pass the method, if not will be bound the wrong context of Group Command
        def create_command_wrapper(method_name):
          async def command(*args, **kwargs):
            dependencies = await resolve_dependencies(cls.__init__)

            instance = cls(**dependencies)
            command = getattr(instance, method_name)

            if asyncio.iscoroutinefunction(command):
              return await command(*args, **kwargs)

            return command(*args, **kwargs)

          return click.Command(
            name=method._cli_command,
            callback=command,
            params=params,
          )

        cli_group.add_command(create_command_wrapper(method_name))

    return cls

  return decorator
