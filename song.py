class Song:
    count = 0  # Class attribute to track total songs
    genres = []  # Class attribute to store unique genres
    artists = []  # Class attribute to store unique artists
    genre_count = {}  # Class attribute to store song count by genre
    artist_count = {}  # Class attribute to store song count by artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1  # Increment song count
        Song.add_to_genres(genre)  # Add genre (handles duplicates)
        Song.add_to_artists(artist)  # Add artist (handles duplicates)
        Song.add_to_genre_count(genre)  # Add to genre count
        Song.add_to_artist_count(artist)  # Add to artist count

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 0
        cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 0
        cls.artist_count[artist] += 1


# Example us