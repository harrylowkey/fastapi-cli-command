import re


def snake_key(text):
  snake_case_text = re.sub(r'[-\s]', '_', text)
  snake_case_text = re.sub(r'(?<!^)(?=[A-Z])', '_', snake_case_text).lower()
  return snake_case_text
