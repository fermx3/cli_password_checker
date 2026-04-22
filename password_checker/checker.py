from password_checker.rules import RULES
from password_checker.models import CheckResult


def _get_label(score: int) -> str:
    """Return a strength label based on the weighted score (0-10)."""
    if score == 10:
        return "strongest"
    if score >= 7:
        return "strong"
    if score >= 4:
        return "normal"
    return "weak"

def check_password(password: str) -> CheckResult:
    """Compares password with defined RULES.

    Args:
        password: Password to check.

    Returns:
        CheckResult datamodel
    """
    failed_rules = []
    score = 0
    for rule in RULES:
        if rule.check(password):
            score += rule.weight
        else:
            failed_rules.append(rule)

    return CheckResult(
        score=score,
        label=_get_label(score),
        failed_rules=failed_rules
    )
