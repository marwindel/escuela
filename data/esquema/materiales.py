class Materiales:
    def __init__(self, id=None, descripcion=None, cantidad=None, aula_id=None, registrado_por=None, fecha_creacion=None, fecha_actualizacion=None  ):
        self.id = id
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.aula_id = aula_id
        self.registrado_por = registrado_por
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion

    def __str__(self):
        return (f'Id: {self.id}, Descripcion: {self.descripcion}, '
                f'Cantidad: {self.cantidad}, Aula_id: {self.aula_id}, Registrado por: {self.registrado_por},  Fecha creacion: {self.fecha_creacion}, Fecha Actualizacion: {self.fecha_actualizacion}')
