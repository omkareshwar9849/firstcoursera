"""
firstcoursera_12345 package.

This package contains the main application and utility functions for the firstcoursera_12345 project.
"""

# Version information
__version__ = "0.1.0"  # This should be updated as the project evolves

# Import specific helpers that we want to make available
try:
    from .utils.helpers import some_helper_function, another_helper_function
except ImportError:
    # If the specific functions don't exist, we'll just pass silently
    pass

# We're not importing anything from main.py or cloud module by default
# Users can import these explicitly if needed

# Define what should be available when someone does `from src import *`
__all__ = ['__version__', 'some_helper_function', 'another_helper_function']

# Remove any names from __all__ that weren't successfully imported
__all__ = [name for name in __all__ if name in globals()]