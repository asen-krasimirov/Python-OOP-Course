from project.song import Song


class Album:
    name: str
    songs: list
    published: bool

    def __init__(self, name: str, *songs: Song):
        self.name = name
        self.songs = []

        for song in list(songs):
            if not song.single:
                self.songs.append(song)

        self.published = False

    def add_song(self, song: Song) -> str:

        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        for hit in self.songs:
            if hit.name == song.name:
                return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:

        if self.published:
            return "Cannot remove songs. Album is published."

        for hit in self.songs:
            if hit.name == song_name:
                self.songs.remove(hit)
                return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:

        if self.published:
            return f"Album {self.name} is already published."  #
        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        album_information = [
            f"Album {self.name}",
            "\n".join(f"== {song.get_info()}" for song in self.songs)
        ]

        if self.songs:
            album_information.append("")

        return '\n'.join(album_information)
