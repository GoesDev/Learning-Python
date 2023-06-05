# 6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
# • Crie uma lista de pessoas que devam participar da enquete sobre linguagem
# favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
# estão.
# 143
# • Percorra a lista de pessoas que devem participar da enquete. Se elas já
# tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por
# responder. Se ainda não participaram da enquete, apresente uma mensagem
# convidando-as a responder.

persons = ['goes', 'julio', 'duda', 'maria', 'turif']

favorite_languages = {
    'goes': 'python',
    'duda': 'java',
    'julio': 'javascript',
    'maria': 'python'
}

for name in persons:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()}!")
    else:
        print(f"Responda a enquete {name.title()}!")
