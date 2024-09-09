from fastapi_cli_command.cli.templates.base_template import BaseTemplate


class CommandTemplate(BaseTemplate):
  def __init__(self, command_name: str):
    self.command_name = command_name
    self.capitalized_module_name = self.capitalize_module_name(command_name)

  def generate_template(self) -> str:
    return f"""from click import Option
from fastapi_cli_command import BaseCommand, command


class CommandOptions:
  REQUIRED_OPTION = Option(
    ['--foo'],
    help='Description for option',
    required=True,
    type=str
  )
  PROMPT_OPTION = Option(
    ['--bar'],
    help='Description for option',
    prompt=True,
    type=int,
    default=99
  )

@command('{self.command_name}')
class {self.capitalized_module_name}Command(BaseCommand):
  def __init__(self):
    pass

  async def run(self, foo: CommandOptions.REQUIRED_OPTION, bar: CommandOptions.PROMPT_OPTION):
    ...
    """
