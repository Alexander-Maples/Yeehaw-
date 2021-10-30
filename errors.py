class Error(Exception):
    """Base class for exceptions in this module."""
    pass
def RaiseShutDown():
  """A way to correctly raise the ShutDown Error"""
  raise ShutDown("The program shutdown")
class ShutDown(Error):
    """Exception raised for internal program uses.
    """
    def __init__(self, details='The program shut down...'):
        self.expression = details