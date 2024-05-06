
'''
CREAR MENU 
PERMITIR ELEGIR 1 POR 1 LAS VECES QUE EL USUARIO DESEE(WHILE) 
PIKACHU ROLL $4500
OTAKU ROLL $5000
PULPO VENENOSO $5200
ANGUILA ELEC ROLL $4800
CODIGO DESCUENTO soyotaku,  10% EN CASO DE INTRODUCIR CODIGO CORRECTAMENTE, CODIGO NO VALIDO EN CASO DE CODIGO INCORRECTO, APRETAR X PARA VOLVER ATRÁS.
MOSTRAR DETALLE DEL PEDIDO (TOTAL PRODUCTOS Y CANTIDAD, Y SI APLICA DESCUENTO)
MOSTRAR  
'''


menu = {
    1: "Pikachu roll $4500",
    2: "Otaku roll $5000",
    3: "Pulpo venenoso $5200",
    4: "Ánguila eléctrica roll $4800"
}

while True:
    
    print("** Menú **\n*Escoja una opción*\n")
    for key, value in menu.items():
        print(f"{key}. {value}")

    opcion = input()

    if opcion.lower() == 'x' or opcion.upper() == 'X':
        break


    if opcion.isdigit():
        opcion = int(opcion)
        if opcion in menu:
            print(f"Seleccionaste {menu[opcion]}")
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
