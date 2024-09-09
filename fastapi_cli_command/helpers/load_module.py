import glob
import importlib


class ModuleHelper:
  def __init__(self, module_paths: list[str]):
    self.paths = module_paths

  def load_modules(self):
    for path in self.paths:
      self._load_module(path)

  def _load_module(self, path: str):
    modules = glob.glob(path, recursive=True)
    for module in modules:
      importlib.import_module(
        module.replace('.py', '').replace('.graphql', '').replace('/', '.').replace('src.', ''),
        package=None,
      )
