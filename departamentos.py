import random

Departamentos = {
    'tolima' : 'ibague',
    'cundinamarca' : 'bogota',
    'antioquia' : 'medellin',
    'bolivar' : 'cartagena',
    'atlantico' : 'barranquilla'
}

while True:
    print("Hola, soy python y voy a elegir un departamento y usted me dice la capital.")
    print("-----------")
    
    departamento_azar = random.choice(list(Departamentos.keys()))
    capital_correcta = Departamentos[departamento_azar]
    
    intentos = 3
    
    while intentos > 0:
        pregunta = input(f"Cual es la capital de {departamento_azar}? Intentos restantes: {intentos}. Si desea irse tan solo escriba (salir): ")
        
        if pregunta.lower() == 'salir':
            print("Hasta luego")
            exit()
        elif pregunta.lower() == capital_correcta.lower():
            print("Bien")
            exit()
        else:
            intentos -= 1
            if intentos == 0:
                print("has agotado tus intentos")
            else:
                print("Incorrecto. Intenta de nuevo")
