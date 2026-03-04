class Usuario:
    def __init__(self, id=None, nombre=None, username=None, clave=None ):
        self.id = id
        self.nombre = nombre
        self.usuario = username
        self.clave = clave

    def __str__(self):
        return (f'Id: {self.id}, '
                f'Nombre: {self.nombre}, '
                f'Usuario:  {self.usuario}, '
                f'Clave: {self.clave}')
