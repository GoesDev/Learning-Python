"""8.8 Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e
o título de um álbum. Depois que tiver essas informações, chame make_album()
com as entradas do usuário e apresente o dicionário criado.
Lembre-se de incluir um valor de saída no laço while."""


def make_album(artist_name, album_title, tracks=""):
    if tracks:
        album = {'Artist': artist_name, 'Title': album_title, 'Tracks': tracks}
    else:
        album = {'Artist': artist_name, 'Title': album_title}
    return album


while True:
    print("\nDigite o nome do Artista e o Título do Album:")
    print("(enter 'q' at any time to quit)")
    art = input("Artista: ")
    if art == 'q':
        break
    tit = input("Album: ")
    if tit == 'q':
        break
    final_album1 = make_album(art, tit)
    print(final_album1)
