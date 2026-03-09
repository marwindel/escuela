class Cliente:
    def __init__(self, id=None, descripcion=None, cantidad=None, registrado_por=None, fecha_creacion=None, fecha_actualizacion=None, grado=None, seccion=None  ):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.registrado_por = registrado_por
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
        self.grado = grado
        self.seccion = seccion

    def __str__(self):
        return (f'Id: {self.id}, Descripcion: {self.descripcion}, '
                f'Cantidad: {self.cantidad}, Registrado por: {self.registrado_por},  Fecha creacion: {self.fecha_creacion}, Fecha Actualizacion: {self.fecha_actualizacion}, Grado: {self.grado}, Seccion: {self.seccion}')
