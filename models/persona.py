from models.enumTipoIdentificacion import EnumTipoIdentificacion

class Persona:
    def __init__(self):
        self.__id = 0
        self.__apellidos = ''
        self.__nombres = ''
        self.__dni = ''
        self.__direccion = ''
        self.__telefono = ''
        self.__tipoIdentificacion = EnumTipoIdentificacion.CEDULA

    @property
    def _tipoIdentificacion(self):
        return self.__tipoIdentificacion

    @_tipoIdentificacion.setter
    def _tipoIdentificacion(self, value):
        self.__tipoIdentificacion = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value

    @property
    def _dni(self):
        return self.__dni

    @_dni.setter
    def _dni(self, value):
        self.__dni = value

    @property
    def _direccion(self):
        return self.__direccion

    @_direccion.setter
    def _direccion(self, value):
        self.__direccion = value

    @property
    def _telefono(self):
        return self.__telefono

    @_telefono.setter
    def _telefono(self, value):
        self.__telefono = value

    # def to_dict(self):
    #     return {
    #         'id': self.__id,
    #         'apellidos': self.__apellidos,
    #         'nombres': self.__nombres,
    #         'dni': self.__dni,
    #         'direccion': self.__direccion,
    #         'telefono': self.__telefono,
    #         'tipo_identificacion': self.__tipo_identificacion.value
    #     }
    
    @property
    def serializable(self):
        return {
            "id": self.__id,
            "apellidos": self.__apellidos,
            "nombres": self.__nombres,
            "direccion": self.__direccion,
            "dni": self.__dni,
            "telefono": self.__telefono,
            "tipo": self.__tipoIdentificacion
        }
    
    def deserializar(data):
        persona = Persona()
        persona.__id = data["id"]
        persona.__apellidos = data["apellidos"]
        persona.__nombres = data["nombres"]
        persona.__direccion = data["direccion"]
        persona.__dni = data["dni"]
        persona.__telefono = data["telefono"]
        persona.__tipoIdentificacion = data["tipo"]
        return persona
        
    def __str__(self) -> str:
        return self.__apellidos + "" + self.__nombres