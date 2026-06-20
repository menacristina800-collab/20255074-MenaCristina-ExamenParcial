class Registro:
    def __init__(self, codigo, carnet_alumno, nombre_empleado, codigo_usuario):
        self.codigo = codigo (str)
        self.carnet_alumno = carnet_alumno (str)
        self.lista = []
        self.bibliotecario_responsable = {"nombre_empleado": nombre_empleado, "codigo_usuario": codigo_usuario}

def agregar_recurso(self, recurso):
    if len(self.lista) >= 4:
        raise ValueError("Limite de recursos por atencion alcanzado")
    self.lista.append(recurso)

def lista_recursos(self):
        return tuple(self.lista)

class Recurso:
    def __init__(self, codigo_identificador, horas_retraso):
        self.codigo_identificador = codigo_identificador (str)
        self.horas_retraso = horas_retraso (int)

class PrestamoLibro(Recurso):
    def calcular_penalizacion(self):
        dias_retraso = self.horas_retraso/24
        return self.dias_retraso * 2.50
    
class UsoSalaEstudio(Recurso):
    def __init__(self, codigo_identificador, horas_retraso, alumnos_espera):
        super().__init__(codigo_identificador, horas_retraso)
        self.alumnos_espera = alumnos_espera (int)

    def calcular_penalizacion(self):
        factor = self.alumnos_espera * 1.5
        return self.horas_retraso * factor
    


class RevisionSaldos:
    def __init__(self, registro):
        self.registro = registro
        self.estado = "CUENTA_ACTIVA"

    def revisar_total_saldos(self):
        total_multas = sum(recurso.calcular_pago() for recurso in self.registro.lista_recursos())
        if total_multas > 15:
            self.estado = "CUENTA_SUSPENDIDA"
        elif recurso.alumnos_espera > 10 for recurso in self.registro.obtener_lista_recursos()):
            self.estado = "CUENTA_SUSPENDIDA"

