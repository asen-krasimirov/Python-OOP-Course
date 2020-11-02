from project.song import Song
from project.album import Album
from project.band import Band


song = Song("Running in the 90s", 3.45, False)
song_1 = Song("Song Two", 3.45, False)
song_2 = Song("Song Three", 3.45, False)
song_3 = Song("Song Four", 3.45, False)

print(song.get_info())
album1 = Album("Initial D", song, song_1)
album2 = Album("Album Two", song_2, song_3)


band = Band("Manuel")
print(band.add_album(album1))
print(band.remove_album("Album Two"))
# print(band.add_album(album2))
print(band.details())

