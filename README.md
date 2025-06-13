# music-collection

The program will keep track of up to 4 albums, and up to 5 songs each album. This must be done using an array (not an
arraylist) to hold the Album objects. Each album will hold up to 5 songs. This must also be done using an array (not an
arraylist).
When run, the program will display a menu of actions to the user, including one that exits the program. Until the user
chooses to exit, the menu is displayed again after each action is completed.
The program should have the following functionalities:
1. Will allow the user to create albums.
The user will specify the album’s name.
There should be an error message if the album already exists, or if there are already 4 albums.
2. Will allow the user to enter a new song into an album.
First, the user will input only the name of the song.
If there are other songs with the same name, the program should list all the details of all the songs with the same
name (album, and song details: name, artist, duration, and genre.) and ask the user if they want to continue. If yes,
the user will input album’s name, song details: name, artist, duration, and genre (note that something – artist,
duration or gender – must be differet). If there are no songs with the same name, there will be a “continue”
option, and the user will input album name and song details.
The program will show an error message if:
• the user input a song that already exists (2 songs are identical if name, artist, duration and genre are the same),
OR
• it is adding a song in an album that exceeds a certain time limit (in song duration times), OR
• the album does not exist, OR
• The album is full
3. Will allow the user to request a list of all songs (and the details of each song) with a specific name.
4. Will allow the user to request a list of all songs (and the details of each song) from an album.
5. Will allow the user to request a list of all albums (including all the songs in each album).
6. Will allow the user to request a list of all songs whose duration is under a certain time (in minutes).
7. Will allow the user to request a list of all songs of a specific genre.
The program should show an appropriate message in case the output of functionalities 3, 4, 5, 6, 7 is none.
8. Will allow the user to delete an album.
There should be an error message if the album does not exist. 
9. Will allow the user to delete a song from an album.
There should be an error message if the album does not exist.
10. Will allow the user input albums and songs from an external file. This option will be just available in the beginning
(before the user input albums and/or songs from keyboard). Follow the format of the ReginaCollection.txt.

https://github.com/Italiant/SENG1110/tree/main
https://github.com/Mohammed-devv/Music-Collection-Manager-Java-OOP-Project/tree/main
