def hacer_retiro(ID, monto):
    consulta_saldo = f'SELECT Saldo FROM Cuentas WHERE ID = {ID}'
    cursor.execute(consulta_saldo)
    saldo_actual = cursor.fetchone()[0]

    if saldo_actual >= monto:
        nuevo_saldo = saldo_actual - monto
        consulta_retiro = f'UPDATE Cuentas SET Saldo = {nuevo_saldo} WHERE ID = {IDCuentas}'
        cursor.execute(consulta_retiro)

        # Registrar la transacción
        consulta_transaccion = f'INSERT INTO Transacciones (IDCuenta, Tipo, Monto, Fecha) VALUES ({IDCuentas}, "retiro", {monto}, NOW())'
        cursor.execute(consulta_transaccion)

        conexion.commit()
        print(f"Retiro de {monto} realizado. Nuevo saldo: {nuevo_saldo}")
    else:
        print("Fondos insuficientes para realizar el retiro.")