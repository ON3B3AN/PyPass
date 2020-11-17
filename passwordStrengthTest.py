import re

passwordRegex = re.compile(r'((^(?=.*[{}\[\]()/\\\'\"`~,;:.<> @#$%!&*])(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])).{8,}$)')


def validate_password_strength(password):
    if passwordRegex.fullmatch(password) is None:
        return False
    else:
        return True
