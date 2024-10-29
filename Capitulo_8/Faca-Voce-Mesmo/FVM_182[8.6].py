"""8.6: Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido."""


def city_country(city_name, country_name):
    full_city_country = city_name + ", " + country_name
    return full_city_country.title()


sp = city_country('são paulo', 'brasil')
tt = city_country('toronto', 'canadá')
tk = city_country('tokyo', 'japão')

print(sp)
print(tt)
print(tk)
