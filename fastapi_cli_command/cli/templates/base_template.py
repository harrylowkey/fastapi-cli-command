import os
import re
from abc import ABC
from pathlib import Path

from fastapi import Path


class BaseTemplate(ABC):
  def __init__(self, name: str):
    self.name = name
    self.base_path = Path(os.getcwd())

  def capitalize_module_name(self, name) -> str:
    split_module_name = re.split(r'[-_]', name)
    capitalized_module_name = ''.join([word.capitalize() for word in split_module_name])
    return capitalized_module_name

  def generate_template(self):
    raise NotImplementedError
