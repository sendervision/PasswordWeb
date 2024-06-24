from string import punctuation, digits, ascii_lowercase, ascii_uppercase, ascii_letters
from random import choice

from schema import PasswordSchema

CONTENT_PASSWORD = "".join([punctuation, ascii_letters, digits])

def get_password(length: int = 8, content_password: str = CONTENT_PASSWORD) -> str:
    length = 40 if length > 40 else length
    password = [choice(content_password) for i in range(length)]
    return "".join(password)


def gen_password(password_data: PasswordSchema.dict_class) -> str:
    content_password = [punctuation, ascii_uppercase, ascii_lowercase]
    length = password_data["input_length_password"]
    is_punctuation = password_data["input_punctuation"]
    is_uppercase = password_data["input_uppercase"]
    is_lowercase = password_data["input_lowercase"]

    list_filters = [is_punctuation, is_uppercase, is_lowercase]
    content_password = [c for _, c in zip(list_filters, content_password) if _]
    content_password = "".join(content_password)
    return get_password(int(length), content_password)

