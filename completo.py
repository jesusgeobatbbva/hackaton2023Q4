import sqlite3
saldo = 0

def registro_usuario(id,nombre,saldo):
    conexion = sqlite3.connect('banco.db')
    cursor = conexion.cursor()
    usuarios = [
        (id, nombre, saldo)]
    cursor.executemany("INSERT INTO Cuentas VALUES(?, ? , ?)", usuarios)
    conexion.commit()
    conexion.close()
    return True
# Función para consultar el saldo de una cuenta
def consultar_saldo(id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Saldo FROM Cuentas WHERE ID=?", (id,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return resultado[0]
    else:
        return None


# Función para realizar un depósito en una cuenta
def realizar_deposito(cuenta_id, monto):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    # Actualizar el saldo en la tabla de Cuentas
    cursor.execute("UPDATE Cuentas SET Saldo = Saldo + ? WHERE ID=?", (monto, cuenta_id))

    # Registrar la transacción en la tabla Transacciones
    cursor.execute("INSERT INTO Transacciones (IDCuenta, Tipo, Monto) VALUES (?, ?, ?)", (cuenta_id, 'deposito', monto))

    conn.commit()
    conn.close()


# Función para realizar un retiro de una cuenta
def realizar_retiro(cuenta_id, monto):
    saldo_actual = consultar_saldo(cuenta_id)

    if saldo_actual is not None and saldo_actual >= monto:
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        # Actualizar el saldo en la tabla de Cuentas
        cursor.execute("UPDATE Cuentas SET Saldo = Saldo - ? WHERE ID=?", (monto, cuenta_id))

        # Registrar la transacción en la tabla Transacciones
        cursor.execute("INSERT INTO Transacciones (IDCuenta, Tipo, Monto) VALUES (?, ?, ?)",(cuenta_id, 'retiro', monto))

        conn.commit()
        conn.close()
        return True
    else:
        return False


# Función para transferir fondos entre dos cuentas
def transferir_fondos(cuenta_origen_id, cuenta_destino_id, monto):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    # Registrar la transacción en la tabla Transacciones para la cuenta origen
    cursor.execute("INSERT INTO Transacciones (IDCuenta, Tipo, Monto) VALUES (?, ?, ?)",(cuenta_origen_id, 'transferencia', -monto))

    # Registrar la transacción en la tabla Transacciones para la cuenta destino
    cursor.execute("INSERT INTO Transacciones (IDCuenta, Tipo, Monto) VALUES (?, ?, ?)",(cuenta_destino_id, 'transferencia', monto))

    conn.close()

    # Realizar el retiro de la cuenta origen y el depósito en la cuenta destino
    if realizar_retiro(cuenta_origen_id, monto):
        realizar_deposito(cuenta_destino_id, monto)
        return True
    else:
        return False


# Función para ver el historial de transacciones de una cuenta
def historial_transacciones(id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Tipo, Monto, Fecha FROM Transacciones WHERE IDCuenta=?", (id,))
    transacciones = cursor.fetchall()

    conn.close()

    return transacciones
def inicio_sesion(id):
    conexion = sqlite3.connect('banco.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombreCliente From Cuentas where ID=?",(id,))
    cliente = cursor.fetchone()
    cliente = ''.join(cliente)
    conexion.close()
    print(f"Bienvenido {cliente}")

from colorama import Back, Fore, Style
# Ejemplo de uso
if _name_ == "_main_":
    while True:
        print(Back.BLACK + Fore.BLUE + Style.BRIGHT + """
        *-------------------*
        | S I M U L A D O R |
        | B A N C A R I O   |
        *-------------------*
        1. Registro Usuario
        2. Consultar saldo
        3. Retiro
        4. Deposito
        5. Transferencia
        6. Historial de transacciones
        7. Salir
        """)

        opcion = input("Seleccione una opción (1/2/3/4/5/6/7/8): ")
        if opcion == '1':
            id = input('Ingresa tu ID: ')
            nombre_cliente = input('Ingresa tu nombre completo: ')
            if registro_usuario(id, nombre_cliente, saldo):
                print('Cuenta registrada exitosamente')
            else:
                print('Cuenta ya existente')
        elif opcion == '2':
            id = input('Ingresa tu id para iniciar sesion: ')
            inicio_sesion(id)

        elif opcion == '3':
            cuenta_id = input("Ingrese el ID de la cuenta: ")
            saldo = consultar_saldo(cuenta_id)
            if saldo is not None:
                print(f"Saldo actual de la cuenta {cuenta_id}: {saldo}")
            else:
                print("Cuenta no encontrada.")

        elif opcion == '4':
            cuenta_id = input("Ingrese el ID de la cuenta: ")
            monto = float(input("Ingrese el monto a depositar: "))
            realizar_deposito(cuenta_id, monto)
            print(f"Depósito de {monto} realizado en la cuenta {cuenta_id}.")

        elif opcion == '5':
            cuenta_id = input("Ingrese el ID de la cuenta: ")
            monto = float(input("Ingrese el monto a retirar: "))
            if realizar_retiro(cuenta_id, monto):
                print(f"Retiro de {monto} realizado en la cuenta {cuenta_id}.")
            else:
                print("Fondos insuficientes o cuenta no encontrada.")

        elif opcion == '6':
            cuenta_origen_id = input("Ingrese el ID de la cuenta de origen: ")
            cuenta_destino_id = input("Ingrese el ID de la cuenta de destino: ")
            monto = float(input("Ingrese el monto a transferir: "))
            if transferir_fondos(cuenta_origen_id, cuenta_destino_id, monto):
                print(
                    f"Transferencia exitosa de {monto} desde la cuenta {cuenta_origen_id} a la cuenta {cuenta_destino_id}.")
            else:
                print("La transferencia no pudo realizarse debido a fondos insuficientes o cuentas no encontradas.")

        elif opcion == '7':
            cuenta_id = input("Ingrese el ID de la cuenta: ")
            transacciones = historial_transacciones(cuenta_id)
            if transacciones:
                print(f"Historial de transacciones de la cuenta {cuenta_id}:")
                for tipo, monto, fecha in transacciones:
                    print(f"Tipo: {tipo}, Monto: {monto}, Fecha: {fecha}")
            else:
                print(f"No hay transacciones para la cuenta {cuenta_id}.")

        elif opcion == '8':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")