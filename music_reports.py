import file_handling

DATA = file_handling.import_data() 
ARTIST = 0
ALBUM_NAME = 1
YEAR = 2
GENRE = 3
LEN_OF_ALBUM = 4
SECONDS = 60


def get_longest_album(albums):
    max_len= 0 
    max_album = None
    for album in albums:
        album_len = (album[LEN_OF_ALBUM].split(":"))
        album_len_sec = int(album_len[0]) * SECONDS + int(album_len[1])
        if album_len_sec > max_len or max_len == 0:
            max_len = album_len_sec
            max_album = album
    return max_album 

def get_shortest_album(albums):
    max_len= 0 
    max_album = None
    for album in albums:
        album_len = (album[LEN_OF_ALBUM].split(":"))
        album_len_sec = int(album_len[0]) * SECONDS + int(album_len[1])
        if album_len_sec < max_len or max_len == 0:
            max_len = album_len_sec
            max_album = album
    return max_album 

def get_albums_by_genre(albums, genre):
    list_of_albums = []
    second_list = []

    for album in albums:
        genre_of_album = album[GENRE]
        second_list.append(genre_of_album)
        if genre_of_album == genre:
            list_of_albums.append(album)
    return list_of_albums 

def get_albums_by_artist(albums, artist):
    list_of_albums = []
    second_list = []

    for album in albums:
        artist_of_album = album[ARTIST]
        second_list.append(artist_of_album)
        if artist_of_album == artist:
            list_of_albums.append(album)
    return list_of_albums 

def get_albums_by_title(albums, title):
    list_of_albums = []
    second_list = []

    for album in albums:
        artist_of_album = album[ALBUM_NAME]
        second_list.append(artist_of_album)
        if artist_of_album == title:
            list_of_albums.append(album)
    return list_of_albums 

# CZAS JESZCZE NIE DZIAŁA :)
def get_albums_by_time(albums, time):
    list_of_albums = []
    second_list = []

    for album in albums:
        artist_of_album = album[LEN_OF_ALBUM]
        second_list.append(artist_of_album)
        if artist_of_album == time:
            list_of_albums.append(album)
    return list_of_albums 

    # 43:00

# MOŻESZ SOBIE SPRAWDZIĆ JAK DZIAŁAJĄ TE FUNKCJE

# get_longest_album(DATA)
# get_shortest_album(DATA)
# print(get_albums_by_genre(DATA, 'pop'))
# print(get_albums_by_artist(DATA, 'Britney Spears'))
# print(get_albums_by_title(DATA, 'Baby One More Time'))
# print(get_albums_by_title(DATA, '42:20'))
# print(get_total_albums_length(DATA))


