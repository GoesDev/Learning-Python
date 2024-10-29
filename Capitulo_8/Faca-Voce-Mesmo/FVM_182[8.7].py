"""8.7 Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas
duas informações. Use a função para criar três dicionários que representem
álbuns diferentes. Apresente cada valor devolvido para mostrar que os
dicionários estão armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar
o número de faixas em um álbum. Se a linha que fizer a chamada incluir um
valor para o número de faixas, acrescente esse valor ao dicionário do álbum.
Faça pelo menos uma nova chamada da função incluindo o número de faixas
em um álbum"""
# person = {'first': first_name, 'last': last_name}


def make_album(artist_name, album_title, tracks=""):
    if tracks:
        album = {'Artist': artist_name, 'Title': album_title, 'Tracks': tracks}
    else:
        album = {'Artist': artist_name, 'Title': album_title}
    return album


final_album1 = make_album('julio', 'od')
final_album2 = make_album('maria', 'od2', 2)
final_album3 = make_album('goes', 'od2', 18)

print(final_album1)
print(final_album2)
print(final_album3)
