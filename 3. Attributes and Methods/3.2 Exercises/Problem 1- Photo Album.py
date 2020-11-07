

class PhotoAlbum:
    pages: int
    photos: list

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.taken_pages = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        return cls(pages)

    def add_photo(self, label: str):
        page = 0
        while True:
            if page == len(self.photos):
                break
            if len(self.photos[page])+1 <= 4:
                self.photos[page].append(label)
                slot = len(self.photos[page])
                return f"{label} photo added successfully on page {page+1} slot {slot}"
            page += 1
        return "No more free spots"

    def display(self):
        page_separator = '-'*11
        information = '\n'.join([page_separator + '\n' + ' '.join(['[]' if slot else ' ' for slot in page]) for page in self.photos])
        return information + '\n' + page_separator + '\n'


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
