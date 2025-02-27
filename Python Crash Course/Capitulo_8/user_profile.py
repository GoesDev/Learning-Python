def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


use_profile = build_profile('albert', 'einstein', location='princeton',
                            field='physics')
print(use_profile)
