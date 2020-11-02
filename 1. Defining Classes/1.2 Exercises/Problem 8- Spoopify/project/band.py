from project.album import Album


class Band:
    name: str
    albums: list

    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:

        for hit in self.albums:
            if hit.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."  #

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:

        for hit in self.albums:
            if hit.name == album_name:

                if hit.published:
                    return f"Album has been published. It cannot be removed."

                self.albums.remove(hit)
                return f"Album {album_name} has been removed."  #

        return f"Album {album_name} is not found."  #

    def details(self) -> str:
        band_information = [
            f"Band {self.name}",
            '\n'.join([album.details() for album in self.albums])
        ]

        if self.albums:
            band_information.append("")

        return "\n".join(band_information)
