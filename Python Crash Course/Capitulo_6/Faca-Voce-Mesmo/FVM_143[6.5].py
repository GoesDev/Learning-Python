# 6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país
# que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
# • Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
# pelo Egito.
# • Use um laço para exibir o nome de cada rio incluído no dicionário.
# • Use um laço para exibir o nome de cada país incluído no dicionário.

rivers = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'justiça': 'sacro império humani'
}

for key, value in rivers.items():
    print(f"O {key.title()} corre pelo {value.title()}.")
