from wtforms import Form

from wtforms import SearchField,PasswordField,EmailField,BooleanField,IntegerField,StringField,SelectMultipleField,RadioField, widgets
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



class CinepolisForm(Form):

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido")
    ])

    compradores = IntegerField("Cantidad de Compradores", [
        validators.DataRequired(message="El campo es requerido")
    ])

    boletos = IntegerField("Cantidad de Boletas", [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(
            min=1,
            max=7,
            message="No se pueden comprar más de 7 boletos por persona"
        )
    ])



class PizzaForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="Campo obligatorio")
    ])

    direccion = StringField("Dirección", [
        validators.DataRequired(message="Campo obligatorio")
    ])

    telefono = StringField("Teléfono", [
        validators.DataRequired(message="Campo obligatorio")
    ])

    piezas = IntegerField("Número de pizzas", [
        validators.DataRequired(message="Campo obligatorio")
    ])

    tamano = RadioField("Tamaño Pizza", choices=[
        ('chica', 'Chica $40'),
        ('mediana', 'Mediana $80'),
        ('grande', 'Grande $120')
    ], validators=[
        validators.DataRequired(message="Campo obligatorio")
    ])

    ingredientes = SelectMultipleField(
    "Ingredientes",
    choices=[
        ('jamon', 'Jamón $10'),
        ('pina', 'Piña $10'),
        ('champinones', 'Champiñones $10')
    ],
    option_widget=widgets.CheckboxInput(),
    widget=widgets.ListWidget(prefix_label=False),
    validators=[validators.DataRequired(message="Campo obligatorio")]
)