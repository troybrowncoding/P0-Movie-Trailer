import media
import fresh_tomatoes

# create empty list of movies
movies = []

# add movies to list with title, box art link, trailer link
movies.append(media.Movie(
    "Braveheart",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "www.youtube.com/watch?v=j53_WxqPZ7c"))

movies.append(media.Movie(
    "Top Gun",
    "http://40.media.tumblr.com/52ecb6d4ea9c404bf51f8602124bf285/tumblr_np6t8jHh3C1uwq4qxo1_500.jpg",  # noqa
    "www.youtube.com/watch?v=VN8ze3S0Uj8"))

movies.append(media.Movie(
    "The Blues Brothers",
    "http://s35.podbean.com/pb/0c35164e351e5177413d83203a57af58/55f5fe6c/data1/blogs24/97450/uploads/blues-brothers-the-mission-from-god.jpg",  # noqa
    "www.youtube.com/watch?v=A-xtJYIwfYo"))

movies.append(media.Movie(
    "Forrest Gump",
    "http://enr.expertcomics.com/images/enr-archives/uploads/2012/11/Forrest-Gump-poster.jpg",  # noqa
    "www.youtube.com/watch?v=eYSnxZKTZzU"))

movies.append(media.Movie(
    "Love Actually",
    "http://d3dvedx3sqrauf.cloudfront.net/i/boxart/zoom/67/60/828765676021.jpg",  # noqa
    "www.youtube.com/watch?v=cYCkFTyADJ0"))

movies.append(media.Movie(
    "Play 'Em Off",
    "http://api.ning.com/files/fRQr8hF1hzOeZMMYwLm632OmoSagRPvVmiZECZTncNtwLX3XZfQF*LBWJykltpwkoOmCk68ROpFHmL*cCf0j7cScrOUL7Y8s/373e104646104437063c99589b485d9b.jpg",  # noqa
    "https://www.youtube.com/watch?v=O2ulyJuvU3Q"))

# generate html file
fresh_tomatoes.create_movie_tiles_content(movies)

# open html file
fresh_tomatoes.open_movies_page(movies)
