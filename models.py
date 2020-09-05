"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Playlist(db.Model):
    """Playlist."""
    __tablename__= "playlists"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    
    play_s = db.relationship('PlaylistSong',
                                  backref='Playlist')

    # direct navigation: emp -> project & back
    song = db.relationship('Song',
                               secondary='playlist_song',
                               backref='playlists')
   

class Song(db.Model):
    """Song."""
    __tablename__= "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    artist = db.Column(db.String(20), nullable=False)
    play_song = db.relationship(
        'Playlist',
        secondary="playlist_song",
        # cascade="all,delete",
        backref="songs",
    )

   


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlist_song"
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)




# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
