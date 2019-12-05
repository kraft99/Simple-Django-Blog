import uuid
from apps.account import models




def _code_exists(code):
    # as private method
    """
    @purpose :
    Return True if code exists else False
    """
    try:
        models.Profile.objects.get(code__iexact = code)
    except models.Profile.DoesNotExist:
        #code does not exists
        return False
    #code exists
    return True


def code_already_taken(code):
    return _code_exists(code)



def generate_code(size = 6):
    """
    @purpose: Generate and return a 6 alphanumeric pin as user's public ID.
    """
    code = str(uuid.uuid4()).replace("-", "").upper()[:size]
    while code_already_taken(code):
        code = str(uuid.uuid4()).replace("-", "").upper()[:size]
    return code





