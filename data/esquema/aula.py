class Aula:
    def __init__(self, id=None, grado=None, seccion=None ):
        self.id = id
        self.grado = grado
        self.seccion = seccion

    def __str__(self):
        return (f'Id: {self.id}, '
                f'Seccion: {self.grado} - {self.seccion}')
