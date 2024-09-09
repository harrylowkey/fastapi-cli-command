import asyncio
from abc import ABC
from typing import ValuesView

from click import Command


class BaseCLI(ABC):
  @staticmethod
  def _run_async(coroutine_function):
    def wrapper(*args, **kwargs):
      return asyncio.run(coroutine_function(*args, **kwargs))

    return wrapper

  def _check_async_function(self, commands: list[Command] | ValuesView[Command]):
    for command in commands:
      original_callback = command.callback
      if asyncio.iscoroutinefunction(original_callback):
        command.callback = self._run_async(original_callback)
