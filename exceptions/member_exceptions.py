class MemberNotFoundError(Exception):
    """Member not found."""
    pass

class DuplicateEmailError(Exception):
    """E-mail already exists."""
    pass

class DuplicateNameError(Exception):
    """Name already exists."""
    pass

class DuplicatePasswordError(Exception):
    """Password already exist."""
    pass

