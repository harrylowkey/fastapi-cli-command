import inspect
from typing import Callable, Optional

from click.core import Parameter


def parse_params(func: Callable) -> Optional[list[Parameter]]:
  signature = inspect.signature(func)
  params = []
  for param in signature.parameters.values():
    try:
      if param.annotation != param.empty:
        params.append(param.annotation)

    except Exception as e:
      raise e
  return params
