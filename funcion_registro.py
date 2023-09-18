import sqlite3

saldo = 0
def registro_usuario(id_cuenta,nombreCliente,saldo):
    conexion = sqlite3.connect("banco.db")
    cursor = conexion.cursor()
    
    cuenta = [(id_cuenta,nombreCliente,saldo)]
    cursor.executemany("INSERT INTO Cuentas VALUES(?,?,?)",cuenta)
    conexion.commit()
    conexion.close()
    
    return True

registro_usuario(2, "Kaeri Silva", saldo)
