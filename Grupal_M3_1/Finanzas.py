import uuid
###################Clase Cliente#######################


class Cliente:  # Se crea la clase cliente
    # se define como parámetros iniciales nombre de cliente, id de cliente y saldo.
    def __init__(self, nombre_cliente, saldo_cliente):
        # Se define que nombre cliente se asignará a futuro.
        self.nombre_cliente = nombre_cliente
        # Se define que el id de cliente sees asignado por el modulo uuid que
        # genera un id unico y con uuid4 el cual genera un id aleatoreo.
        self.id_cliente = uuid.uuid4()
        # Se define que el saldo de cliente se asignará a futuro.
        self.saldo_cliente = saldo_cliente

    # Metodo Clase Cliente
    def girar(self, cantidad_giro):  # Se define el parámetro cantidad de giro
        # Se define que cantidad de giro se asignará a futuro.
        self.cantidad_giro = cantidad_giro
        # Se define que el saldo cliente que se solicite a futuro será el saldo menos la cantidad girada.
        self.saldo_cliente = self.saldo_cliente - self.cantidad_giro
        # se solicita que la función otorgue como resultado la cantidad de giro.
        return self.cantidad_giro

    # se define la función abonar con el parámetro a definir de cantidad de abono.
    def abonar(self, cantidad_abono):
        # se define que cantidad de abono será asignado a futuro.
        self.cantidad_abono = cantidad_abono
        # se define que el saldo del cliente será dicho monto mas la cantidad abonada.
        self.saldo_cliente = self.saldo_cliente + self.cantidad_abono
        # la función arrojará como resultado la cantidad abonada.
        return self.cantidad_abono

    # función para mostrar saldo sin parámetros por asignar.
    def mostrar_saldo(self):
        # se define que el resultado de la función será un str predefinido con dos self a llamar: nombre de cliente + saldo de cliente.
        return "El saldo de {} es: {}".format(self.nombre_cliente, self.saldo_cliente)


################Clase Financiera#####################


class Financiera:
    def __init__(self, nombre_financiera, saldo_institucional):
        self.nombre_financiera = nombre_financiera
        self.id_financiera = uuid.uuid4()
        self.saldo_institucional = saldo_institucional
        self.clientes = []

    def agregar_cliente(self, id_cliente):
        self.id_cliente = id_cliente
        return self.clientes.append(self.id_cliente)

    def eliminar_cliente(self, indice):
        self.indice = indice
        return self.clientes.pop(self.indice)

    def transferir():
        return True

    def giros_totales():
        return True

    def abonos_totales():
        return True

    def mostrar_saldo_institucional():
        return True
