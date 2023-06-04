favorite_languages = {
    'goes': 'python',
    'duda': 'java',
    'julio': 'javascript',
    'maria': 'python'
}

# print(f"Duda's favorite language is {favorite_languages['duda'].title()}.")

# for name in favorite_languages.keys():
#     print(name.title())

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking poll')

print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    if language == 'php':
        print(f"{language.upper()}")
    else:
        print(f"{language.title()}")
