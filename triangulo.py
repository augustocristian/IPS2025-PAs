def es_equilatero(lado1: float, lado2: float, lado3: float) -> bool:

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return False
    
    if (lado1 + lado2 <= lado3) or (lado1 + lado3 <= lado2) or (lado2 + lado3 <= lado1):
        return False
    
    return lado1 == lado2 == lado3