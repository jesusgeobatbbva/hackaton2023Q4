import sqlite3
import datetime
from forex_python.converter import CurrencyRates

conexion = sqlite3.connect('banco.db')

cursor =  conexion.cursor()

cursor.execute("CREATE TABLE Cuentas(ID INTEGER PRIMARY KEY AUTOINCREMENT, nombreCliente TEXT NOT NULL, saldo DECIMAL(10,2) NOT NULL)")
cursor.execute("CREATE TABLE Transacciones(ID INTEGER  PRIMARY KEY AUTOINCREMENT, IDCuenta INTEGER ,Tipo TEXT NOT NULL, Monto DECIMAL(10,2)NOT NULL, Fecha DATETIME, FOREIGN KEY(IDCuenta) REFERENCES Cuentas(ID))")


#Funcion Deposito
def deposito(monto, cuenta_id):
    cursor.execute("UPDATE Cuentas SET saldo = saldo + ? WHERE ID = ?", (monto, cuenta_id))
    fecha_actual = datetime.date.today()
    fecha = fecha_actual.strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO Transacciones (IDCuenta, Tipo, Monto, Fecha) VALUES (?, ?, ?, ?)",
                   cuenta_id, 'Depósito', monto, fecha)
    cursor.commit()
    print("Transacción Exitosa")


#Funcion Transacciones

def historial_transacciones(id_cuenta):
    cursor.execute("SELECT * FROM Transacciones WHERE IDCuenta = ?", id_cuenta)
    return cursor.fetchall()

#Funcion Extra, Cambio de Monedas

def convertir_pesos_a_otras_monedas(cantidad):
    cr = CurrencyRates()
    monedas = ['EUR', 'USD', 'GBP', 'KRW', 'JPY']
    tasas = {}
    
    for moneda in monedas:
        tasa = cr.get_rate('MXN', moneda)
        tasas[moneda] = tasa
    
    for moneda, tasa in tasas.items():
        conversion = round(cantidad * tasa, 2)
        print(f"{cantidad} Pesos Mexicanos son aproximadamente {conversion} {moneda}")


cursor.close()