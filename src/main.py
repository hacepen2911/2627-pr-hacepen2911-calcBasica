def sumar(numero1:float, numero2:float):
    """Suma de numero1 y numero2

    :param numero1: El primer numero solicitado
    :param numero2: El segundo numero solicitado

    :return Resultado de la suma entre numero1 y numero2:
    """
    resultado_suma = numero1 + numero2
    return resultado_suma

def restar(numero1:float, numero2:float):
    """Resta de numero1 y numero2

    :param numero1: El primer numero solicitado
    :param numero2: El segundo numero solicitado

    :return Resultado de la resta entre numero1 y numero2:
    """    
    resultado_resta = numero1 - numero2
    return resultado_resta

def multiplicar(numero1:float, numero2:float):
    """Multiplicacion de numero1 y numero2
    
    :param numero1: El primer numero solicitado
    :param numero2: El segundo numero solicitado

    :return Resultado de la multiplicacion entre numero1 y numero2:
    """
    resultado_multipicacion = numero1 * numero2
    return resultado_multipicacion

def dividir(numero1:float, numero2:float):
    """Division de numero1 y numero2
    
    :param numero1: El primer numero solicitado
    :param numero2: El segundo numero solicitado

    :return Resultado de la division entre numero1 y numero2 o mensaje de error:
    """
    if numero2 == 0:
        resultado_division = "No se puede dividir por 0"
    else:
        resultado_division = numero1 / numero2
    return resultado_division


def main():
    numero1 = float(input("Introduce el primer numero: "))
    numero2 = float(input("Introduce el segundo numero: "))

    resultado_suma:float = sumar(numero1, numero2)
    resultado_resta:float = restar(numero1, numero2)
    resultado_multiplicacion:float = multiplicar(numero1, numero2)
    resultado_division:float = dividir(numero1, numero2)

    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicación: {resultado_multiplicacion}")
    print(f"División: {resultado_division}")
    
if __name__ == "__main__":
    main()