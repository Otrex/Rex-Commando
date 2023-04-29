class SupportedOSException(Exception):
  pass

class IncorrectPassword(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__("Password is incorrect")