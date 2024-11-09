# 3.5 Alterando a lista de convidados: Você acabou de saber que um de seus
# convidados não poderá comparecer ao jantar, portanto será necessário enviar
# um novo conjunto de convites. Você deverá pensar em outra pessoa para chamar

names = ['Goes', 'Duda', 'Turif']

for name in names:
    print(f'{name}, quero te convidar para jantar!')

print(f"Infelizmente {names[2]} não poderá comparecer")

names[2] = "Muwdur"

for name in names:
    print(f'{name}, quero te convidar para jantar!')
