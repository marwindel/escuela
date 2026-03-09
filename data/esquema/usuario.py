class Usuario:
    def __init__(self, id_user=None,  username=None, nombre=None, clave=None, fecha_reg=None ):
        self.id = id_user
        self.usuario = username
        self.nombre = nombre
        self.clave = clave
        self.fecha_reg = fecha_reg

    def __str__(self):
        return (f'Id: {self.id}, '
                f'Usuario:  {self.usuario}, '
                f'Nombre: {self.nombre}, '
                f'Clave: {self.clave}, '
                f'Fecha: {self.fecha_reg}')
