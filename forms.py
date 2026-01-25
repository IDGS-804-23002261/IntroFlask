from wtforms import Form

from wtforms import SearchField,PasswordField,EmailField,BooleanField,IntegerField,StringField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido")
    ])
    nombre=StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])
    apellido=StringField("Apellido", [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=EmailField("correo", [
        validators.Email(message="Ingresa Correo Valido")
    ])



