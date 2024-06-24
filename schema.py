from marshmallow import fields, Schema
from typing import Optional
from sqlmodel import Field, SQLModel

class PasswordSchema(Schema):
    input_password = fields.String(load_default="")
    input_punctuation = fields.Bool(load_default = True)
    input_uppercase = fields.Bool(load_default = True)
    input_lowercase = fields.Bool(load_default = True)
    input_length_password = fields.Integer(load_default = 6)
    input_digit = fields.Bool(load_default = True, required = False)

class Password(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: Optional[str] = Field(default="", min_length=4)
    passwd: str
    is_punctuation: bool
    is_uppercase: bool
    is_lowercase: bool
