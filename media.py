# movie class and contructor


class Movie:
    """ These keep movie titles, posters, and trailers together."""
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Creates a movie with title, poster,
        and trailer info all as strings.
        Be sure to include complete URL's.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
