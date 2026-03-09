from escuela.aula import Aula
from escuela.conexion import Conexion
from escuela.cliente import Cliente
from escuela.usuario import Usuario
import bcrypt


class ClienteDAO:
    SELECCIONAR = 'SELECT m.id, m.descripcion, m.cantidad, u.nombre as registrado_por, m.fecha_creacion, m.fecha_actualizacion, a.grado, a.seccion FROM materiales as m INNER JOIN aula as a ON (m.aula_id = a.id) INNER JOIN usuario as u ON (m.registrado_por=u.id) ORDER BY m.id'
    SELECCIONAR_AULA = 'SELECT * FROM aula'
    SELECCIONAR_USUARIO = 'SELECT * FROM usuario'
    SELECCIONAR_EXISTE_AULA = 'SELECT COUNT(*) AS valor FROM materiales WHERE aula_id=%s'
    SELECCIONAR_EXISTE_USUARIO = 'SELECT COUNT(*) AS valor FROM materiales WHERE registrado_por=%s'

    SELECT_ID = 'SELECT id FROM aula WHERE grado=%s AND seccion=%s'
    INSERTAR_MAT = 'INSERT INTO materiales(descripcion, cantidad, aula_id, registrado_por, fecha_creacion, fecha_actualizacion) VALUES(%s, %s, %s, %s, %s, %s)'
    INSERTAR_AULA = 'INSERT INTO aula(grado, seccion) VALUES(%s, %s)'
    INSERTAR_USUARIO = 'INSERT INTO usuario(username, nombre, password) VALUES(%s, %s, %s)'


    ACTUALIZAR = 'UPDATE materiales SET descripcion=%s, cantidad=%s, aula_id=%s, fecha_actualizacion=%s WHERE id=%s'
    ACTUALIZAR_USER_DATOS = 'UPDATE usuario SET nombre=%s, username=%s WHERE id=%s'
    ACTUALIZAR_USER_CLAVE = 'UPDATE usuario SET password=%s WHERE id=%s'


    ELIMINAR_MAT = 'DELETE FROM materiales WHERE id=%s'
    ELIMINAR_AULA = 'DELETE FROM aula WHERE id=%s'

    @classmethod
    def login(cls, username, password):
        conexion = None
        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            query = f"SELECT * FROM usuario WHERE username ='{username}'"
            cursor.execute(query)
            registros = cursor.fetchone()
            # Mapeo de clase-tabla cliente

            if registros:

                password_hash = registros[3]
                usuario_id = registros[0]
                 # Asumiendo que tu tabla tiene una columna 'password'
                if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
                    return usuario_id
                else:
                    return 0
            else:
                return False
            
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionarUsuario(cls):
        conexion = None
        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_USUARIO)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            usuarios = []
            for registro in registros:
                user = Usuario(registro[0], registro[1],
                                  registro[2], registro[3], registro[4])
                usuarios.append(user)
            return usuarios
            
        except Exception as e:
            print(f'Ocurrio un error al seleccionar usuarios: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            cliente = []
            for registro in registros:
                clientes = Cliente(registro[0], registro[1],
                                  registro[2], registro[3], registro[4], registro[5], registro[6], registro[7])
                cliente.append(clientes)
            return cliente
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def seleccionarAula(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_AULA)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            aula = []
            for registro in registros:
                aulas = Aula(registro[0], registro[1],
                                  registro[2])
                aula.append(aulas)
            return aula
        except Exception as e:
            print(f'Ocurrio un error al seleccionar aulas: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def aulaSelect(cls, seccion):
        conexion = None
        try:

            datos = seccion.split("-")
            grado = datos[0].strip()
            seccion = datos[1].strip()

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECT_ID, (grado, seccion))
            registros = cursor.fetchall()
            # Mapeo de clase-t
            return registros[0][0]
        except Exception as e:
            print(f'Ocurrio un error al seleccionar aulas: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def aulaValid(cls, seccion):
        conexion = None
        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_EXISTE_AULA, [seccion])
            registros = cursor.fetchall()
            # Mapeo de clase-t
            return registros[0][0]
        except Exception as e:
            print(f'Ocurrio un error al seleccionar aulas: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def userValid(cls, seccion):
        conexion = None
        try:

            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR_EXISTE_USUARIO, [seccion])
            registros = cursor.fetchall()
            # Mapeo de clase-t
            return registros[0][0]
        except Exception as e:
            print(f'Ocurrio un error al seleccionar aulas: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def insertarMat(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.descripcion, cliente.cantidad, cliente.aula_id, cliente.registrado_por, cliente.fecha_creacion, cliente.fecha_actualizacion)
            cursor.execute(cls.INSERTAR_MAT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un Material: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertarAula(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.grado, cliente.seccion)
            cursor.execute(cls.INSERTAR_AULA, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un Aula: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def insertarUsuario(cls, usuario):
        conexion = None
        try:

            # Generamos un 'salt' y hasheamos
            salt = bcrypt.gensalt()
            clave_encrytada = bcrypt.hashpw(usuario.clave.encode('utf-8'), salt)
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (usuario.nombre, usuario.usuario, clave_encrytada)
            cursor.execute(cls.INSERTAR_USUARIO, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar un Usuario: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.descripcion, cliente.cantidad,
                       cliente.aula_id, cliente.fecha_actualizacion, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un material: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def actualizarUsuarioDatos(cls, usuarios):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = ( usuarios.nombre,
                       usuarios.usuario, usuarios.id)
            cursor.execute(cls.ACTUALIZAR_USER_DATOS, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un material: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizarUsuarioClave(cls, usuarios):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            # Generamos un 'salt' y hasheamos
            salt = bcrypt.gensalt()
            clave_encrytada = bcrypt.hashpw(usuarios.clave.encode('utf-8'), salt)
            valores = (clave_encrytada, usuarios.id_user)
            cursor.execute(cls.ACTUALIZAR_USER_CLAVE, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar un material: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminarMat(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR_MAT, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un material: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminarAula(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR_AULA, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un aula: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    
    @classmethod
    def eliminarUsuario(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR_AULA, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar un aula: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


if __name__ == '__main__':
    # Insertar cliente
    # cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    # Actualizar cliente
    # cliente_actualizar = Cliente(3, 'Alexa', 'Tellez', 400)
    # clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    # print(f'Clientes actualizados: {clientes_actualizados}')

    # Eliminar cliente
    #cliente_eliminar = Cliente(id=3)
    #clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    #print(f'Clientes eliminados: {clientes_eliminados}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)