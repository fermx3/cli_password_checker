import re
from password_checker.models import Rule

RULES: list[Rule] = [
    Rule(
        name="length",
        check=lambda p: len(p) >= 8,
        feedback="Password must be at least 8 characters long"
    ),
    Rule(
        name="uppercase",
        check=lambda p: bool(re.search(r"[A-Z]", p)),
        feedback="Add at least one uppercase letter (A-Z)"
    ),
    Rule(
        name="lowercase",
        check=lambda p: bool(re.search(r"[a-z]", p)),
        feedback="Add at least one lowercase letter (a-z)"
    ),
    Rule(
        name="digit",
        check=lambda p: bool(re.search(r"[0-9]", p)),
        feedback="Add at least one digit (0-9)"
    ),
    Rule(
        name="special_character",
        check=lambda p: bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-]", p)),
        feedback="Add at least one special character (!@#$%^&*)"
    )
]
