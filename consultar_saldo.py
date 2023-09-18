def consultar_saldo(conexion, id_cuenta):
    cursor = conexion.cursor()
    saldo = cursor.execute('SELECT Saldo FROM Cuentas WHERE ID = ?', (id_cuenta,)).fetchone()[0]
    return float(saldo.replace(',', '.'))