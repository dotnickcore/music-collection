import constants

def print_main_menu():
    print()
    print('Music Collection - Main Menu')
    print('------------------------------')
    print('1: Go To Album Management Menu')
    print('2: Go To Song Management Menu')
    print('3: Go To Artist Management Menu')
    print('4: Go To Genre Management Menu')
    print('5: Go To Statistic Menu')
    print('-1: Exit Application')
    print()

def print_album_menu():
    print()
    print('Music Collection - Album Menu')
    print('------------------------------')
    print('1: Create Album')
    print('2: Delete Album')
    print('3: Search Album')
    print('4: Get List of Albums')
    print('-1: Go Back To Main Menu')
    print()

def print_song_menu():
    print()
    print('Music Collection - Song Menu')
    print('------------------------------')
    print('1: Create Song')
    print('2: Delete Delete')
    print('3: Search Song')
    print('4: Filter by Genre')
    print('5: Filter by Duration')
    print('-1: Go Back To Main Menu')
    print()


def print_artist_menu():
    print()
    print('Music Collection - Artist Menu')
    print('------------------------------')
    print('1: Create Artist')
    print('2: Delete Artist')
    print('3: Search Artist')
    print('4: Get List of Artist')
    print('-1: Go Back To Main Menu')
    print()

def print_genre_menu():
    print()
    print('Music Collection - Genre Menu')
    print('------------------------------')
    print('1: Create Genre')
    print('2: Delete Genre')
    print('3: Get All Genres')
    print('-1:Go Back To Main Menu')
    print()

def print_statistics_menu():
    print()
    print('Music Collection - Statistics Menu')
    print('------------------------------')
    print('1: Album Count')
    print('2: Song Count')
    print('3: Artist Count')
    print('4: Genre Count')
    print('5: Average Song Duration on Album')
    print('6: Longest Song on Album')
    print('7: Shortest Song on Album')
    print('-1: Go Back To Main Menu')
    print()

def get_main_menu_choice():
    print_main_menu()


def get_album_menu_choice():
    pass

def get_song_menu_choice():
    pass

def get_artist_menu_choice():
    pass

def get_genre_menu_choice():
    pass

def get_statistics_menu_choice():
    pass

def main():
    # initialize the user's choice
    choice = 0

    while choice != constants.Constants.QUIT:
        choice = get_main_menu_choice()

    pass

if __name__ == "__main__":
    main()