import webbrowser

class Movie():
        def __init__(self, movie_title, movie_storyline, movie_poster_url,  movie_trailer_youtube, movie_release):
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_url = movie_poster_url
            self.trailer_youtube_url = movie_trailer_youtube
            self.release = movie_release
        def show_trailer(self):
            webbrowser.open(self.trailer_youtube_url)