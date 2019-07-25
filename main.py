import file_handling
import music_reports
import display

while True:

    display.print_start_menu(music_reports.DATA)
    answer = input("What would you like to do? ")
    print('----------------------------------------------------------------------------------------')

    if answer == '*':
        display.print_multiple_albums(music_reports.DATA)
    elif answer == 'g':
        answer = input("Which genre? ")
        display.print_multiple_albums(music_reports.get_albums_by_genre(music_reports.DATA, answer))
    elif answer == 't':
        answer = input("Album should be longer than? ")
        if answer.isnumeric():    
            album_name = input("Album should be shorter than? ")
            if album_name.isnumeric(): 
                display.print_multiple_albums(music_reports.get_albums_by_time(music_reports.DATA, answer, album_name))
        else:
            print('----------------------------------------------------------------------------------------')
            print("STOP ACTING LIKE A CHILD AND CHOOSE A TIMELINE FFS!!!")
            print('----------------------------------------------------------------------------------------')
            continue
    elif answer == 's':
        display.print_single_album(music_reports.get_shortest_album(music_reports.DATA))
    elif answer == 'l':
        display.print_single_album(music_reports.get_longest_album(music_reports.DATA))
    elif answer == 'a':
        answer = input("Which artist? ")
        display.print_multiple_albums(music_reports.get_albums_by_artist(music_reports.DATA, answer))
    elif answer == 'n':
        answer = input("Which name? ")
        display.print_multiple_albums(music_reports.get_albums_by_title(music_reports.DATA, answer))
    elif answer == '-':
        answer = input("Artist please:")
        album_name = input("Name please:")
        music_reports.delete_record(music_reports.DATA, answer, album_name)
    elif answer == '+':
        artist = input("Artist please:")
        album_name = input("Name please:")
        year = input("Year please:")
        genre = input("Genre please:")
        time = input("Time please:")
        music_reports.add_record(music_reports.DATA, artist, album_name, year, genre, time)
    elif answer == 'e':
        file_handling.export_data(music_reports.DATA, 'external_file.txt', mode="w")
    elif answer == 'q':
        exit()
    else:
        print("Pick a valid letter!!! Geez...")
    print('----------------------------------------------------------------------------------------')