# 7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
# número é múltiplo de dez ou não

number = int(input("Informe um número: "))

if number % 10 == 0:
    print(f"{number} é múltiplo de 10")
else:
    print(f"{number} não é múltiplo de 10")
