class MemberNotFoundError(Exception):
    """Member not found."""
    pass

class DuplicateEmailError(Exception):
    """E-mail already exists."""
    pass