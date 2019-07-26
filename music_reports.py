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

def get_albums_by_time(albums, timemin, timemax):
    list_of_albums = []
    second_list = []
    min=int(timemin)
    max=int(timemax)
    for album in albums:
        album_len = album[LEN_OF_ALBUM]
        minutes = int(album_len.split(':')[0])
        second_list.append(album_len)
        if minutes > min and minutes < max: #z zakresu
            list_of_albums.append(album)
    return list_of_albums 

def delete_record(albums, number):
    i = 1
    for album in albums:
        if int(number) == i:
            albums.remove(album)
        i += 1

            # file_handling.export_data(albums, mode="w")
    return albums        

def add_record(albums, artist, album_name, year, genre, time):
    album = [artist, album_name, year, genre, time]
    if album in albums:
        print("Already in the music database!")
    else:
        albums.append(album)

    # file_handling.export_data(albums, mode="w")


    # 43:00

# MOŻESZ SOBIE SPRAWDZIĆ JAK DZIAŁAJĄ TE FUNKCJE

# get_longest_album(DATA)
# get_shortest_album(DATA)
# print(get_albums_by_genre(DATA, 'pop'))
# print(get_albums_by_artist(DATA, 'Britney Spears'))
# print(get_albums_by_title(DATA, 'Baby One More Time'))
# print(get_albums_by_time(DATA, '40','45'))
# print(get_total_albums_length(DATA))

# display.print_single_album(get_longest_album(DATA))
# display.print_multiple_albums(DATA)

