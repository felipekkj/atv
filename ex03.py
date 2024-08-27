import math

def area_triangulo(a, b, c):
    # Calcula o semi-perímetro
    s = (a + b + c) / 2
    # Calcula a área usando a fórmula de Heron
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Entrada do usuário
a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))

if a + b > c and a + c > b and b + c > a:
    print(f"A área do triângulo é: {area_triangulo(a, b, c):.2f}")
else:
    print("Os valores fornecidos não formam um triângulo válido.")
