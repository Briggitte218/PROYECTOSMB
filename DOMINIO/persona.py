import re

class Persona:
    """
    Clase que permite crear objetos de tipo persona
    """
    def __init__(self, cedula: str, nombre: str, apellido: str, sexo: str, email: str = None):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.email = email

    # Cedula
    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor.isdigit():
            raise ValueError("La cédula debe contener solo números")
        self._cedula = valor


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.isalpha():
            raise ValueError("El nombre debe contener solo letras")
        self._nombre = valor.capitalize()


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor.isalpha():
            raise ValueError("El apellido debe contener solo letras")
        self._apellido = valor.capitalize()


    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        if valor.lower() not in ["masculino", "femenino", "prefiero no decirlo"]:
            raise ValueError("Sexo debe ser 'Masculino', 'Femenino' o 'Prefiero no decirlo'")
        self._sexo = valor.lower()


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor is None:
            self._email = None
        else:
            patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(patron, valor):
                raise ValueError("Email inválido, digite correctamente")
            self._email = valor

    # Representación en cadena
    def __str__(self):
        return f'Persona: {self.nombre} {self.apellido}, Cédula: {self.cedula}, Sexo: {self.sexo}, Email: {self.email}'