from colorama import Back, Fore, Style
from funcion_registro import registro_usuario
import sqlite3
import datetime

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
opcion = int(input("Ingresa una opcion: "))

match opcion:
    
    case 1:
        nombreCuenta = input("Ingresa tu nombre completo: ")
        if registro_usuario(nombreCuenta,saldo):
            print("Registro de usuario exitosamente!")
        else:
            print("Usuario ya existente")
    case 2:
        #Consuta saldo
    case 3:
        #Retiro
    case 4:
        #Deposito
    case 5: 
        id_o = input("Ingrese el ID de la cuenta origen: ")
        id_d = input("Ingrese el ID de la cuenta destino: ")
        m = input("Ingrese el monto/cantidad a enviar: ")

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
                print("Transferencia exitosa! ")

            cursor.close()

        transferencias(id_o, id_d , m)

            
    case 6:
        #Historial de transacciones 
    case 7:
        print("Saliendo...")
        print("Vuelva pronto :)")   
    case _: 
        print("Opcion no valida")     