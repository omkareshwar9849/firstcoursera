import re
import uuid
from datetime import datetime

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def format_date(date: datetime, format_string: str = "%Y-%m-%d") -> str:
    """
    Format a datetime object to a string.

    Args:
        date (datetime): The datetime object to format.
        format_string (str): The format string to use. Defaults to "%Y-%m-%d".

    Returns:
        str: The formatted date string.
    """
    return date.strftime(format_string)

def generate_unique_id() -> str:
    """
    Generate a unique identifier.

    Returns:
        str: A unique identifier string.
    """
    return str(uuid.uuid4())

def sanitize_input(input_string: str) -> str:
    """
    Sanitize user input by removing any potentially harmful characters.

    Args:
        input_string (str): The input string to sanitize.

    Returns:
        str: The sanitized input string.
    """
    # Remove any HTML tags
    sanitized = re.sub(r'<[^>]*?>', '', input_string)
    # Remove any non-alphanumeric characters except spaces and common punctuation
    sanitized = re.sub(r'[^a-zA-Z0-9\s.,!?-]', '', sanitized)
    return sanitized.strip()

def truncate_string(string: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length, appending a suffix if truncated.

    Args:
        string (str): The string to truncate.
        max_length (int): The maximum length of the string.
        suffix (str): The suffix to append if the string is truncated. Defaults to "...".

    Returns:
        str: The truncated string.
    """
    if len(string) <= max_length:
        return string
    return string[:max_length - len(suffix)] + suffix

def is_valid_username(username: str) -> bool:
    """
    Check if a username is valid.

    A valid username should:
    - Be between 3 and 20 characters long
    - Contain only alphanumeric characters and underscores
    - Start with a letter

    Args:
        username (str): The username to validate.

    Returns:
        bool: True if the username is valid, False otherwise.
    """
    username_regex = r'^[a-zA-Z][a-zA-Z0-9_]{2,19}$'
    return re.match(username_regex, username) is not None

# You can add more helper functions as needed for your specific project requirements