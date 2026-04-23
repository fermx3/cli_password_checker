import getpass
from password_checker.checker import check_password

def main():
    password = getpass.getpass("Enter password: ")

    result = check_password(password)

    score = result.score
    score_bar = "█" * score + "░" * (10 - score)
    label = result.label
    failed_rules = result.failed_rules

    print("Password received. \n")
    print("-" * 10, "Results:", "-" * 10)
    print(f"Score: {score}/10 {score_bar} {label.title()}")
    print("-" * 30, "\n")

    for failed_rule in failed_rules:
        print(f"- {failed_rule.feedback}")

    if not failed_rules:
        print("✓ Your password meets all requirements.")
