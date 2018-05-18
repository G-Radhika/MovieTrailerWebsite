"""
      Class defination.
      Class Movies
      Args:
            movie_title (str):      Title of the movie.
            movie_stroyline(str):   Gives an abrigde Story line.
            poster_image (url):     Url for the movie's poster art.
            trailer_youtube(url):   Movies trailer from YouTube.
      Class Methods:
            show_trailer is the only class method defined.
            It takes one argument as input - tailer_youtube and
            plays the link on the webbrowser.
"""

import webbrowser

class Movie():
      def __init__(self, movie_title, movie_stroyline, poster_image, trailer_youtube):
            self.title = movie_title
            self.storyline = movie_stroyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube

      def show_trailer(self):
            webbrowser.open(self.trailer_youtube)