def historial_transacciones(IDCuenta):
    consulta = f'SELECT * FROM Transacciones WHERE IDCuenta = {IDCuenta}'
    cursor.execute(consulta)
    transacciones = cursor.fetchall()

    if transacciones:
        print(f"Historial de transacciones para la cuenta {IDCuenta}:")
        for transaccion in transacciones:
            print(f"ID: {transaccion[0]}, Tipo: {transaccion[2]}, Monto: {transaccion[3]}, Fecha: {transaccion[4]}")
    else:
        print(f"No se encontraron transacciones para la cuenta {IDCuenta}")