def somar(num1, num2):
    resp = num1 + num2
    print(resp)
def dividir(num1, num2):
    resp = num1 / num2
    print(resp)
def diminuir(num1, num2):
    resp = num1 - num2
    print(resp)
def multi(num1, num2):
    resp = num1 * num2
    print(resp)
def piramide(qtd):
    for x in range(qtd+1):
        print(str(x) * x)
def piramide_espaço(qtd):
    for x in range(1,qtd+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()
def total_vogais(texto):
    contador = 0
    for x in texto:
        if x in "aeiouAEIOU":
            contador+=1
    print(f"O total de vogais é de {contador}")
def estoque(produto,qtd,valor):
    estoqueTotal = qtd * valor
    return estoqueTotal
def pos_neg(num):
    if num > 0:
        return ("P")
    elif num < 0:
        return ("N")
    else:
        return ("Z")
