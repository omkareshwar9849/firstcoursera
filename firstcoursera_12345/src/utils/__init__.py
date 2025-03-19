"""
Utility module for the firstcoursera_12345 project.

This package contains various helper functions and utilities used across the project.
"""

import os

# Check if helpers.py exists
if not os.path.exists(os.path.join(os.path.dirname(__file__), 'helpers.py')):
    raise ImportError("helpers.py is missing from the utils package")

from .helpers import *

# TODO: Replace the wildcard import with explicit imports of helper functions
# once helpers.py is finalized. For example:
# from .helpers import function1, function2, HelperClass

# Define __all__ to control what's imported with "from utils import *"
__all__ = []  # TODO: Populate this list with the names of importable objects from helpers.py