def print_single_album(album):
        print(' | '.join(album))

def print_multiple_albums(albums):
        for album in albums:
                print(' | '.join(album))

def print_start_menu(albums):
        print("Music database")
        print("Currently, there are ", len(albums))
        print("* - display all albums")
        print("g - display albums by genre")
        print("t - display albums from giving time range")
        print("s - display shortest album")
        print("s - display longest album")
        print("a - display albums by artist")
        print("n - display albums by name")
        print("v - view playlist")

def print_add_playlist():
        print("Would you like to add this track to playlist?")

