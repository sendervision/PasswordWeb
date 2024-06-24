import json
from flask import Flask, render_template, request, Response, jsonify, redirect
from marshmallow import ValidationError

from src.password import get_password, gen_password
from schema import PasswordSchema, Password
from db.db import db_add_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/<int:length>")
def main(length: int = 8):
    data = {}
    get_default_values = PasswordSchema().load({})
    if request.method == "GET":
        password = get_password(length)
        data = {**get_default_values, "password": password}
    elif request.method == "POST":
        if not request.form:
            return redirect("/")
        data_form_password = dict(request.form.items())
        input_password = data_form_password.get("input_password", get_default_values["input_password"])
        input_uppercase = data_form_password.get("input_uppercase", False)
        input_lowercase = data_form_password.get("input_lowercase", False)
        input_punctuation = data_form_password.get("input_punctuation", False)
        input_length_password = data_form_password.get("input_length_password", get_default_values["input_length_password"])
        schema_passwd = PasswordSchema()

        passwd_data = {
            "input_password": input_password, 
            "input_uppercase": input_uppercase, 
            "input_lowercase": input_lowercase,
            "input_punctuation": input_punctuation,
            "input_length_password": input_length_password
        }
        try:
            result = schema_passwd.load(passwd_data)
            passwd = gen_password(passwd_data)
            passwd_data["password"] = passwd
            data = passwd_data
        except ValidationError as error:
            return jsonify(error.messages), 400
        
    return render_template("index.html", data=data)

    if not request.data:
        return jsonify('data required'), 400

    data = json.loads(request.data)
    schema = PasswordSchema()
    try:
        result = schema.load(data)
        password = gen_password(result)
    except ValidationError as error:
        return jsonify(error.messages), 400
    else:
        password = Password(
            passwd = result["input_password"],
            is_uppercase = result["input_uppercase"],
            is_lowercase = result["input_lowercase"],
            is_punctuation = result["input_punctuation"],
        )
        db_add_password(password)
    return Response("Mot de passe enregistré avec succès", status=200)
