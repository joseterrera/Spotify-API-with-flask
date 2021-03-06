from flask import Flask, redirect, render_template, request, session, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong, User
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm, RegisterForm, LoginForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///new_music'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    print("****************session************")
    print(session["username"])
    print(session["user_id"])

    print("****************session************")


    return render_template("index.html")

##############################################################################
# auth routes

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user: produce form & handle form submission."""
    # print('$$$$$$$$$$$$$$$$$$$$$$')
    # print('$$$$$$$$$$$$$$$$$$$$$$')
    # print('$$$$$$$$$$$$$$$$$$$$$$')
    # print('$$$$$$$$$$$$$$$$$$$$$$')

    # print('session', session )
    

    if 'user_id' in session:
        return redirect(f"/users/{session['user_id']}")

    form = RegisterForm()
    username = form.username.data
    password = form.password.data

    existing_user_count = User.query.filter_by(username=name).count()
    if existing_user_count > 0:
        flash("User already exists")
        return redirect('/login')

    if form.validate_on_submit():
        user = User.register(username, password)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        # session['username'] = user.username
        # print('heeee')
        print(user.id)
        session['user_id'] = user.id
        print('id', session['user_id'])

        return redirect(f"/users/{user.id}")

    else:
        return render_template("users/register.html", form=form)





@app.route("/login", methods=["GET", "POST"])
def login():
    """Produce login form or handle login."""

    if "user_id" in session:
        return redirect(f"/users/{session['user_id']}")

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)  # <User> or False
        if user:
            # session['username'] = user.username
            return redirect(f"/users/{user.id}")
        else:
            form.username.errors = ["Invalid username/password."]
            return render_template("users/login.html", form=form)

    return render_template("users/login.html", form=form)

@app.route("/logout")
def logout():
    """Logout route."""
    if "user_id" in session:
        session.pop("username")
    return redirect("/login")



@app.route("/users/<int:user_id>", methods=["GET", "POST"])
def profile(user_id):
    """Example hidden page for logged-in users only."""
    # return redirect("/")

    # if form.validate_on_submit():
    # if "username" not in session or username != session['username']:
    if session.get["user_id"] not in session:
        flash("You must be logged in to view!")
        return redirect("/")
    # user = User.query.get(username)
    form = PlaylistForm()
    playlists = Playlist.query.filter_by(user_id=session['user_id']).all()
    # print('%%%%%%%%%%%%%%%%%%$')
    # username = User.query.get(username)
    # print(username)
    
    if form.validate_on_submit():
        
        
        name = form.name.data
        new_playlist = Playlist(name=name, user_id=session['user_id'])
        db.session.add(new_playlist)
        db.session.commit()
        playlists.append(new_playlist)

    return render_template("users/profile.html", playlists=playlists, form=form)



# @app.route("/logout")
# def logout():
#     """Logs user out and redirects to homepage."""

#     session.pop("user_id")
#     # session.pop("username")

#     return redirect("/")


##############################################################################
# Playlist routes


# @app.route("/playlists")
# def show_all_playlists():
#     """Return a list of playlists."""

#     playlists = Playlist.query.all()

#     return render_template("playlist/playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    playlist = Playlist.query.get_or_404(playlist_id)
    songs = PlaylistSong.query.filter_by(playlist_id=playlist_id)

    for b in songs:
        print('testing',b)


    return render_template("playlist/playlist.html", playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()

    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        new_playlist = Playlist(name=name, description=description)
        db.session.add(new_playlist)
        db.session.commit()
        # flash(f"Added {name} at {description}")
        return redirect("/profile")

    return render_template("playlist/new_playlist.html", form=form)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("song/songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    song = Song.query.get_or_404(song_id)
    playlists = song.play_song


    return render_template("song/song.html", song=song, playlists=playlists)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form = SongForm()
    # songs = Song.query.all()

    if form.validate_on_submit():
        title = request.form['title']
        artist = request.form['artist']
        new_song = Song(title=title, artist=artist)
        db.session.add(new_song)
        db.session.commit()
        return redirect("/songs")

    return render_template("song/new_song.html", form=form)



@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""
    
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to songs not already on this playlist

    curr_on_playlist = [s.id for s in playlist.songs]
    form.song.choices = (db.session.query(Song.id, Song.title).filter(Song.id.notin_(curr_on_playlist)).all())

    if form.validate_on_submit():

        # This is one way you could do this ...
        playlist_song = PlaylistSong(song_id=form.song.data, playlist_id=playlist_id)
        db.session.add(playlist_song)

        # Here's another way you could that is slightly more ORM-ish:
        #
        # song = Song.query.get(form.song.data)
        # playlist.songs.append(song)

        # Either way, you have to commit:
        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")

    return render_template("song/add_song_to_playlist.html", playlist=playlist, form=form)