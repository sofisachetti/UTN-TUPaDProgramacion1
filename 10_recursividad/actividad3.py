'''
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1). Prueba esta función en un
algoritmo general.

Por ejemplo sería:
2³ = 2 x 2²
2² = 2 × 2¹
2¹ = 2 × 2⁰
'''

def potencia(base, exponente):
    if exponente == 0:  # la base sería el numero elevado a 0 = 1
        return 1

    return base * potencia(base, exponente - 1)  # hay que ir restandole 1 al exponente

base = int(input("Base: "))  # pido base y potencia al usuario
exp = int(input("Exponente: "))
resultado = potencia(base, exp)
print(f"{base}^{exp} = {resultado}")
