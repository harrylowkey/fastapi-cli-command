def cli_command(name: str):
  def decorator(func):
    func._cli_command = name
    return func

  return decorator
