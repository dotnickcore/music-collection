
class MainMenu:
    # Main Menu Choices
    ALBUM_MANAGEMENT = 1
    SONG_MANAGEMENT = 2
    ARTIST_MANAGEMENT = 3
    GENRE_MANAGEMENT = 4
    STATISTICS_MANAGEMENT = 5
    QUIT = -1

class AlbumMenu:
    # Album Menu Choices
    CREATE_ALBUM = 1
    DELETE_ALBUM = 2
    GET_ALBUM_DETAILS = 3
    LIST_ALBUMS = 4
    ALBUM_MENU_BACK = -1

class SongMenu:
    # Song Menu Choices
    ADD_SONG = 1
    DELETE_SONG = 2
    SEARCH_SONG = 3
    FILTER_BY_GENRE = 4
    FILTER_BY_DURATION = 5
    SONG_MENU_BACK = -1

class ArtistMenu:
    # Artist Menu Choices
    ADD_ARTIST = 1
    DELETE_ARTIST = 2
    SEARCH_ARTIST = 3
    GET_ARTISTS = 4
    ARTIST_MENU_BACK = -1

class GenreMenu:
    # Genre Menu Choices
    ADD_GENRE = 1
    DELETE_GENRE = 2
    GET_ALL_GENRES = 3
    GENRE_MENU_BACK = -1

class StatisticsMenu:
    # Statistics Menu Choices
    ALBUMS_COUNT = 1
    SONG_COUNT = 2
    ARTIST_COUNT = 3
    GENRE_COUNT = 4
    AVERAGE_SONG_DURATION = 5
    LONGEST_SONG = 6
    SHORTEST_SONG = 7
    STATISTICS_MENU_BACK = -1