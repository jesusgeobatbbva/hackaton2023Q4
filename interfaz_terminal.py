from colorama import Back, Fore, Style
from funcion_registro import registro_usuario

if __name__ == '__main__':
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
                #Tansferencia
            case 6:
                #Historial de transacciones 
            case 7:
                print("Saliendo...")
                print("Vuelva pronto :)")
                break   
            case _: 
                print("Opcion no valida")     