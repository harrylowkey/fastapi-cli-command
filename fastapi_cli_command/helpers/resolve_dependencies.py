from contextlib import AsyncExitStack

from fastapi import Request
from fastapi.dependencies.utils import get_dependant, solve_dependencies


async def resolve_dependencies(callable_instance):
  dependant = get_dependant(path='/', call=callable_instance)

  async with AsyncExitStack() as stack:
    request = Request(
      {
        'type': 'http',
        'headers': [],
        'query_string': '',
        'fastapi_astack': stack,
      }
    )

    try:
      values, errors, _, _, _ = await solve_dependencies(request=request, dependant=dependant, async_exit_stack=stack)
      if errors:
        # FIXME: handle errors because of incorrect path '/':  [{'type': 'missing', 'loc': ('query', 'self'), 'msg': 'Field required', 'input': None, 'url': 'https://errors.pydantic.dev/2.6/v/missing'}]
        pass
    except Exception as e:
      print('Exception during dependency resolution:', e)
      raise

    return values
