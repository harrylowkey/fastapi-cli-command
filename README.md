# FastAPI CLI Command

FastAPI CLI Command package helps you:

- Automatically generate CLI commands.
- Construct command modules in a clean and organized manner.
- Automatically inject dependencies into your commands.

By utilizing the click package behind the scenes, the commands can leverage features such as command arguments, options, command groups, and more.

## Dependencies

- fastapi
- click


## Installation
```bash
pip install fastapi_cli_command
```

## Command generation

0. Export PYTHONPATH environment variable

```bash
export PYTHONPATH=*path-to-your-project/src/*
```

1. Generate single command

```bash
fastapi_cli_command generate command --path {path}
```

Example:
To generate single command, run:

```
fastapi_cli_command generate command --path src/users/commands --name test
```

*Note: You can omit the --name option from the CLI command, as click will prompt you for input.*

This will create a file at src/users/commands/single-command.py with the following content:

```python
# src/users/commands/test_command.py
from click import Option
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

@command('test')
class TestCommand(BaseCommand):
  def __init__(self):
    pass

  async def run(self, foo: CommandOptions.REQUIRED_OPTION, bar: CommandOptions.PROMPT_OPTION):
    ...
    
```

2. Generate group command

```bash
fastapi_cli_command generate group-command --path={path}
```

Example:
To generate a group seeder command, run:

```bash
fastapi_cli_command generate group-command --path src/seed/commands --name seeder
```

```python
# src/seed/commands/seeder_command.py
from click import Option
from fastapi_cli_command import cli_command, cli_command_group

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

@cli_command_group('seeder')
class SeederGroupCommand:
  def __init__(self):
    pass

  @cli_command('REPLACE_ME')
  async def command(self, foo: CommandOptions.REQUIRED_OPTION, bar: CommandOptions.PROMPT_OPTION):
    ...

  @cli_command('REPLACE_ME')
  async def command_2(self):
    ...
    
```

### When to use?

#### Scenario 1: Seeding Data into the Database
If you want to seed user and post data into the database, you can create a group command:

```bash
fastapi_cli_command generate group-command --path src/seed/commands --name seed
```

```python

from click import Option
from fastapi_cli_command import cli_command, cli_command_group

class CommandOptions:
  USER_QUANTITY = Option(
    ['--quantity'],
    help='How many users that you want to generate',
    required=True,
    prompt=True,
    type=int
  )
  POST_QUANTITY = Option(
    ['--quantity'],
    help='How many users that you want to generate',
    type=int,
    default=99
  )

@cli_command_group('seed')
class SeedGroupCommand:
  def __init__(self, user_repo: UserRepository = Depends(), post_repo: PostRepository = Depends()):
    self.user_repo = user_repo
    self.post_repo = post_repo

  @cli_command('user')
  async def seed_user(self, quantity: CommandOptions.USER_QUANTITY):
    ...

  @cli_command('post')
  async def seed_post(self, quantity: CommandOptions.POST_QUANTITY = None):
    ...
    
```

Then, you can run the following commands:

```bash
fastapi_cli_command seed user
fastapi_cli_command seed post --quantity 10
```


#### Scenario 2: Updating a User's Username
If you want to update a user's username using their email address, you can create a single command:

```bash
fastapi_cli_command generate command --path src/users/commands --name update-username
```

```python
from click import Option
from fastapi_cli_command import BaseCommand, command

class CommandOptions:
  EMAIL = Option(
    ['--email'],
    help='Email address of user that you want to update',
    prompt=True,
    required=True,
    type=str,
  )
  USERNAME = Option(
    ['--username'],
    help='Username that you want to replace',
    required=True,
    prompt=True,
    type=str,
  )

@command('update-username')
class UpdateUsernameCommand(BaseCommand):
  def __init__(self, user_repo: UserRepository = Depends()):
    self.user_repo = user_repo

  async def get_user_by_email(self, email: str):
    ...

  async def update_username_by_email(self, user_id: UUID, username: str):
    ...

  async def run(self, email: TestCommandOptions.EMAIL, username: TestCommandOptions.USERNAME):
    user = await self.get_user_by_email(email)
    await self.update_username_by_email(user.id, username)

```
