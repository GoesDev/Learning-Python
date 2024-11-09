"""8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome
e o sobrenome, além de três outros pares chave-valor que o descrevam."""


def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


jcgois_profile = build_profile('júlio', 'gois', location='são paulo',
                               field='administração')
megomes_profile = build_profile('maria', 'goes', location='são paulo',
                                field='administração')
gmsantos_profile = build_profile('gilberto', 'miguel', location='carapicuiba')

print(jcgois_profile)
print(megomes_profile)
print(gmsantos_profile)
