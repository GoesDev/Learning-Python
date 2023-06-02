# 6.2 – Números favoritos: Use um dicionário para armazenar os números
# favoritos de algumas pessoas. Pense em cinco nomes e use-os como chaves em
# dicionário. Pense em um número favorito para cada pessoa e armazene cada
# um como um valor em seu dicionário. Exiba o nome de cada pessoa e seu
# número favorito. Para que seja mais divertido ainda, faça uma enquete com
# alguns amigos e obtenha alguns dados reais para o seu programa.

person_numbers = {
    'duda': '1',
    'goes': '25',
    'turif': '3'
}

for i in person_numbers:
    print(i.title(), person_numbers[i])
