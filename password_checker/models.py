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

@dataclass
class CheckResult:
    """Represents a single result in the password_ckecker.checker

    Attributes:
        score: Strength score from 0 to 10. 0-2 Weak, 3-5 Medium, 6-8 Strong, 9-10 Strongest.
        label: Word description of the score.
        failed_rules: A list of the rules that failed.
    """
    score: int
    label: str
    failed_rules: list[Rule]
