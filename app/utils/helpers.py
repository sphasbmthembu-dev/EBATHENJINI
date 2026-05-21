"""Helper functions for EBATHENJINI."""

from datetime import datetime


def format_date(date_obj, format_string='%Y-%m-%d'):
    """Format a date object to string.
    
    Args:
        date_obj: Date object to format
        format_string: Format string (default: YYYY-MM-DD)
    
    Returns:
        Formatted date string
    """
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime(format_string)


def get_current_date():
    """Get current date as string.
    
    Returns:
        Current date in YYYY-MM-DD format
    """
    return datetime.now().strftime('%Y-%m-%d')


def validate_memory_data(title, description):
    """Validate memory data before saving.
    
    Args:
        title: Memory title
        description: Memory description
    
    Returns:
        Tuple (is_valid, error_message)
    """
    if not title or not title.strip():
        return False, "Title cannot be empty"
    
    if not description or not description.strip():
        return False, "Description cannot be empty"
    
    if len(title) > 100:
        return False, "Title too long (max 100 characters)"
    
    return True, ""
