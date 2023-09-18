import sqlite3

conexion = sqlite3.connect('banco.db')

cursor =  conexion.cursor()

cursor.execute("CREATE TABLE Cuentas(ID INTEGER PRIMARY KEY AUTOINCREMENT, nombreCliente TEXT NOT NULL, saldo DECIMAL(10,2) NOT NULL)")
cursor.execute("CREATE TABLE Transacciones(ID INTEGER  PRIMARY KEY AUTOINCREMENT, IDCuenta INTEGER ,Tipo TEXT NOT NULL, Monto DECIMAL(10,2)NOT NULL, Fecha DATETIME, FOREIGN KEY(IDCuenta) REFERENCES Cuentas(ID))")

cursor.close()