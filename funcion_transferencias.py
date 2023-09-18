import sqlite3
import datetime

conexion = sqlite3.connect('banco.db')
cursor =  conexion.cursor()

def transferencias(id_origen, id_destino, monto):
    date = datetime.datetime.now()
    date_now = date.strftime("%d/%m/%Y")

    #ver si el origen tiene saldo
    saldoactual = cursor.execute("SELECT saldo "
    "FROM Cuentas "
    "WHERE ID = %s ;",(id_origen))

    if float(saldoactual) < float(monto):
        print("No cuenta con el saldo suficiente para realizar esta operación")
    else:
        #query para transacciones
        cursor.execute("INSERT INTO Transacciones (IDCuenta, Tipo, Monto, Fecha) "
        " VALUES (%s, %s, %s, %s) ;",(int(id_origen), "Transferencia", float(monto), date_now))

        #monto restado
        cursor.execute("UPDATE Cuentas "
        "SET Saldo = Saldo - %s "
        "WHERE ID = %s ;", (float(monto), id_origen))

        #monto agregado
        cursor.execute("UPDATE Cuentas "
        "SET Saldo = Saldo + %s "
        "WHERE ID = %s ;", (float(monto), id_destino))

    cursor.close()