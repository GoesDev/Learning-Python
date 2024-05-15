# 8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
#  nome de uma cidade e seu país. A função deve exibir uma frase simples, como
#  Reykjavik está localizada na Islândia. Forneça um valor default ao
#  parâmetro que representa o país. Chame sua função para três cidades
#  diferentes em que pelo menos uma delas não esteja no país default.

def describe_city(cidade, pais='brasil'):
    print(cidade.title() + " está localizada no(a) " + pais.title() + ".")


describe_city("são paulo")
describe_city("carapicuíba")
describe_city("tokyo", "japão")
