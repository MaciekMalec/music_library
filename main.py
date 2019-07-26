import file_handling
import music_reports
import display
import time


while True:

    display.print_start_menu(music_reports.DATA)
    
    answer = input("What would you like to do? ")
    print('----------------------------------------------------------------------------------------')

    if answer == '*':
        display.print_multiple_albums(music_reports.DATA)
    elif answer == 'g':
        answer=display.print_specific_type(music_reports.DATA,3)
        # answer = input("Which genre? ")
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
        answer2 = display.print_specific_type(music_reports.DATA,0)
        print('----------------------------------------------------------------------------------------')
        display.print_multiple_albums(music_reports.get_albums_by_artist(music_reports.DATA, answer2))
    elif answer == 'n':
        answer2 = display.print_specific_type(music_reports.DATA,1)
        print('----------------------------------------------------------------------------------------') 
        display.print_multiple_albums(music_reports.get_albums_by_title(music_reports.DATA, answer2))
    elif answer == '-':
        answer2 = ''
        while answer2 != '0':
            display.print_multiple_albums(music_reports.DATA)
            answer2 = input("Number of album to remove, please or 0 to go back:")
            music_reports.delete_record(music_reports.DATA, answer2)
    elif answer == '+':
        display.print_multiple_albums(music_reports.DATA)
        ok=False
        artist = input("Artist please:")
        album_name = input("Name please:")
        if album_name != '':
            year = input("Year please:")
            if year.isdigit() and int(year) > 0:
                genre = input("Genre please:")
                time_input = input("Time please:")
                try:
                    time_formated = time.strptime(time_input, '%H:%M')
                    music_reports.add_record(music_reports.DATA, artist, album_name, year, genre, time_input)
                    ok=True
                except: 
                    if time_input.isdigit():
                        time_input=':'.join([time_input,'00'])
                        music_reports.add_record(music_reports.DATA, artist, album_name, year, genre, time_input)
                        ok=True
                     
        if ok:
            print('album ', artist, album_name, year, genre, time_input,' added')
        else:
            print('----------------------------------------------------------------------------------------')
            print("INVALID INPUT!")
    elif answer == 'e':
        file_handling.export_data(music_reports.DATA, 'external_file.txt', mode="w")
    elif answer == 'q':
        exit()
    else:
        print("Pick a valid letter!!! Geez...")
    print('----------------------------------------------------------------------------------------')