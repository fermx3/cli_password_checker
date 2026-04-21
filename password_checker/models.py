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
    weight: int

@dataclass
class CheckResult:
    """Represents a single result in the password_ckecker.checker

    Attributes:
        score: Strength score from 0 to 10. 0-3 Weak, 4-6 Medium, 7-9 Strong, 10 Strongest.
        label: Word description of the score.
        failed_rules: A list of the rules that failed.
    """
    score: int
    label: str
    failed_rules: list[Rule]
