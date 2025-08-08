top_level_domains = [".com", ".org", ".net"]


def validate_name(name):
    if not name or not name.strip():
        return False

    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'")

    # generator expression
    # (filtering_condition | for variable in iterable )
    # [output_if_true | for variable in iterable | if condition]  # vs list comp
    return all(char in allowed_chars for char in name)


def validate_email(email):
    try:
        local, domain = email.split("@")
    except BaseException:
        return False

    if not local or not domain:
        return False

    if "." not in domain:
        return False

    if not any(domain.endswith(tld) for tld in top_level_domains):
        return False

    return True


def validate_password(password):
    if len(password) < 8:
        return False

    if not any(char.isdigit() for char in password):
        return False

    return True
