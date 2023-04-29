import json
import subprocess
import pexpect
from errors import IncorrectPassword

class ExecutorResult:
  output = None
  error = None
  code = None

  def __init__(self, output=None, error=None, code=None, fnc = None):
    self.code = code
    self.output = output
    self.error = error

  def __getitem__(self, key):
    if (key == 'output'):
      return self.output
    if (key == 'error'):
      return self.error
    if (key == 'code'):
      return self.code

  def to_json(self):
    return json.dumps({
      "output": self.output,
      "error": self.error,
      "code": self.code
    })

  def __str__(self):
    return self.to_json()


class Executor:
  @staticmethod
  def sudo_executor(command, password = ""):
    sudo_command = f"echo '{password}' | sudo -kS {command}"

    print(f"=> Executing sudo command: {command}")

    process = subprocess.Popen(
      sudo_command, 
      shell=True, 
      stdout=subprocess.PIPE, 
      stderr=subprocess.PIPE
    )

    stdout_lines = []
    stderr_lines = []

    for line in process.stdout:
      stdout_lines.append(line.decode().strip())

    for line in process.stderr:
      stderr_lines.append(line.decode().strip())

    pattern = [
      'Password:Sorry, try again.',
      'sudo: no password was provided', 'sudo: 1 incorrect password attempt'
    ]

    code = process.wait()

    if any(s in stderr_lines for s in pattern):
        raise IncorrectPassword()

    return ExecutorResult(stdout_lines, stderr_lines, 0)

  @staticmethod
  def executor(command):
    print(f"=> Executing command: {command}")

    process = subprocess.Popen(
      command, 
      shell=True, 
      stdin=subprocess.PIPE, 
      stdout=subprocess.PIPE, 
      stderr=subprocess.PIPE
    )

    stdout_lines = []
    stderr_lines = []

    for line in process.stdout:
      stdout_lines.append(line.decode().strip())

    for line in process.stderr:
      stderr_lines.append(line.decode().strip())

    code = process.wait()

    return ExecutorResult(stdout_lines, stderr_lines, code)
