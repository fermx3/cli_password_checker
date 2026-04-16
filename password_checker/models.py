from dataclasses import dataclass
from typing import Callable

@dataclass
class Rule:
    """Represents a single rule in the password_checker

    Attributes:
        name: Rule name to identify it.
        check: Function that takes a password and returns bool.
        feedback: Feedback message shown when the rule fails.
    """
    name: str
    check: Callable[[str], bool]
    feedback: str
