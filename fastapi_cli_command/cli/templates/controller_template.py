from fastapi_cli_command.cli.templates.base_template import BaseTemplate


class ControllerTemplate(BaseTemplate):
  def __init__(self, controller_name: str):
    self.name = controller_name
