import constants
import menu

def access_album_menu():
    menu_loop = True

    while menu_loop:
        menu.load_album_menu()

        again = True

        while again:
            try:
                choice = int(input('Enter your choice [1-4]: '))
                again = False
            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if choice == constants.AlbumMenu.CREATE_ALBUM:
            menu_loop = True
        elif choice == constants.AlbumMenu.DELETE_ALBUM:
            menu_loop = True
        elif choice == constants.AlbumMenu.GET_ALBUM_DETAILS:
            menu_loop = True
        elif choice == constants.AlbumMenu.LIST_ALBUMS:
            menu_loop = True
        elif choice == constants.AlbumMenu.ALBUM_MENU_BACK:
            menu_loop = False
            break
        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

def access_song_menu():
    menu_loop = True

    while menu_loop:
        menu.load_song_menu()

        again = True

        while again:
            try:
                choice = int(input('Enter your choice [1-5]: '))
                again = False
            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if choice == constants.SongMenu.ADD_SONG:
            menu_loop = True
        elif choice == constants.SongMenu.DELETE_SONG:
            menu_loop = True
        elif choice == constants.SongMenu.SEARCH_SONG:
            menu_loop = True
        elif choice == constants.SongMenu.FILTER_BY_GENRE:
            menu_loop = True
        elif choice == constants.SongMenu.FILTER_BY_DURATION:
            menu_loop = True
        elif choice == constants.SongMenu.SONG_MENU_BACK:
            menu_loop = False
            break
        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

def access_artist_menu():
    menu_loop = True

    while menu_loop:
        menu.load_artist_menu()

        again = True

        while again:
            try:
                choice = int(input('Enter your choice [1-4]: '))
                again = False
            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if choice == constants.ArtistMenu.ADD_ARTIST:
            menu_loop = True
        elif choice == constants.ArtistMenu.DELETE_ARTIST:
            menu_loop = True
        elif choice == constants.ArtistMenu.SEARCH_ARTIST:
            menu_loop = True
        elif choice == constants.ArtistMenu.GET_ARTISTS:
            menu_loop = True
        elif choice == constants.ArtistMenu.ARTIST_MENU_BACK:
            menu_loop = False
            break
        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

def access_genre_menu():
    menu_loop = True

    while menu_loop:
        menu.load_genre_menu()

        again = True

        while again:
            try:
                choice = int(input('Enter your choice [1-3]: '))
                again = False
            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if choice == constants.GenreMenu.ADD_GENRE:
            menu_loop = True
        elif choice == constants.GenreMenu.DELETE_GENRE:
            menu_loop = True
        elif choice == constants.GenreMenu.GET_ALL_GENRES:
            menu_loop = True
        elif choice == constants.GenreMenu.GENRE_MENU_BACK:
            menu_loop = False
            break
        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

def access_statistics_menu():
    menu_loop = True

    while menu_loop:
        menu.load_statistics_menu()

        again = True

        while again:
            try:
                choice = int(input('Enter your choice [1-7]: '))
                again = False
            except ValueError:
                # catches input errors
                # input error message
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if choice == constants.StatisticsMenu.ALBUMS_COUNT:
            menu_loop = True
        elif choice == constants.StatisticsMenu.SONG_COUNT:
            menu_loop = True
        elif choice == constants.StatisticsMenu.ARTIST_COUNT:
            menu_loop = True
        elif choice == constants.StatisticsMenu.GENRE_COUNT:
            menu_loop = True
        elif choice == constants.StatisticsMenu.AVERAGE_SONG_DURATION:
            menu_loop = True
        elif choice == constants.StatisticsMenu.LONGEST_SONG:
            menu_loop = True
        elif choice == constants.StatisticsMenu.SHORTEST_SONG:
            menu_loop = True
        elif choice == constants.StatisticsMenu.STATISTICS_MENU_BACK:
            menu_loop = False
            break
        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

def main():
    # initialize the user's choice
    menu_loop = True

    while menu_loop:
        menu.load_main_menu()

        again = True

        while again:
            try:
                choice = int(input('Enter your choice [1-5]: '))
                again = False
            except ValueError:
                print("Oops, Invalid Error!")
                print("Please Try Again!")
                again = True

        if choice == constants.MainMenu.ALBUM_MANAGEMENT:
            access_album_menu()
            menu_loop = True

        elif choice == constants.MainMenu.SONG_MANAGEMENT:
            access_song_menu()
            menu_loop = True

        elif choice == constants.MainMenu.ARTIST_MANAGEMENT:
            access_artist_menu()
            menu_loop = True

        elif choice == constants.MainMenu.GENRE_MANAGEMENT:
            access_genre_menu()
            menu_loop = True

        elif choice == constants.MainMenu.STATISTICS_MANAGEMENT:
            access_statistics_menu()
            menu_loop = True

        elif choice == constants.MainMenu.QUIT:
            menu_loop = False
            break

        else:
            # any other input will print an error message
            print("Oops, Something went wrong!")
            print("Please Try Again!")

if __name__ == "__main__":
    main()