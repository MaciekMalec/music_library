def print_single_album(album):
        print(' | '.join(album))

def print_multiple_albums(albums):
        i = 1
        for album in albums:
                print(i, '-', ' | '.join(album))
                i+=1
def print_specific_type(albums,type):
        i=0
        amount=[]
        amount.append(0)
        lista=[]
        for album in albums:
                if  album[type] not in lista:
                        lista.append(album[type])
                        amount.append(1)
                else:
                        j=1
                        for item in lista:
                                if album[type]==item:
                                        amount[j]+=1
                                else:
                                        j+=1
        i=1
        for item in lista:
                print(i, ' - ', item, ' - ', amount[i], ' albums.')
                i+=1
        ans=input('Which one do you chose? ')
        if str.isdigit(ans) and int(ans)<=len(lista):
                ans=lista[int(ans)-1]
        return ans

def print_start_menu(albums):
        print("Music database")
        print("Currently, there are ", len(albums), " albums")
        year=[]
        timem=[]
        times=[]
        time=[]
        for i in range(0, len(albums)):
                year.append(int(albums[i][2]))
                timem.append(int(albums[i][4].split(":")[0]))
                times.append(int(albums[i][4].split(":")[1]))
                time.append(timem[i]*60+times[i])
        yearmax=max(year)
        timemax=max(time)
        yearmin=min(year)
        timemin=min(time)
        maxt=[(timemax-timemax%60)/60, timemax%60]
        mint=[(timemin-timemin%60)/60, timemin%60]
        print("Longest album is ", int(maxt[0]),":",int(maxt[1]))
        print("Shortest album is ", int(mint[0]),":",int(mint[1]))
        print("Oldest album is from ", yearmin)
        print("Most recent is from ", yearmax)
        print("* - display all albums")
        print("g - display albums by genre")
        print("t - display albums from giving time range")
        print("s - display shortest album")
        print("l - display longest album")
        print("a - display albums by artist")
        print("n - display albums by name")
        print("- - delete an album")
        print("+ - add an album")
        print("e - save album to external file")
        print("q - exit program")

def print_add_playlist():
        print("Would you like to add this track to playlist?")
                







