def get_formatted_name(first_name, last_name, middle_name=""):
    """Devolve um nome completo de modo elegante"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
name = get_formatted_name('júlio', 'goes', middle_name='cesar')
print(name)
