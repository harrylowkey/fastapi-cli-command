from abc import ABC, abstractmethod


class BaseCommand(ABC):
  @abstractmethod
  def run(self, *args, **kwargs):
    raise NotImplementedError