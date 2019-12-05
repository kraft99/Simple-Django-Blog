""" use in situations where users are to register with email and password"""
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model



def is_email_taken(email):
    """ validates if email is taken """
    try:
        get_user_model().objects.get(email__iexact = email)
    except get_user_model().DoesNotExist:
        return False
    return True



def get_username_from_email(email):
    """ retrieve username from email """
    if email and not is_email_taken(email):
        username = email.split('@')[:-1]
        return "".join(username)



def get_clean_username(email):
    """ username with all dots replaced with userscore """
    dot = '.'
    under_score = '_'
    if not email is None:
        username = get_username_from_email(email)
        if username:
            if dot in username:
                return username.replace(dot,under_score).strip()
            return username.strip()
        else:
            pass




def username_already_exist(email):
    """ validates without username is taken """
    try:
        username = get_clean_username(email)
        username = get_user_model().objects.get(username__iexact = username)
    except get_user_model().DoesNotExist:
        return False
    return True



def generate_username(email):
    """
    @dependents : 
    get_clean_username
    username_already_exist
    get_username_from_email

    1. append random number to username is its taken
    Example :
    username : edward_mike  to edward_mike123 (only when its taken)

    """
    pass
