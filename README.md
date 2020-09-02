
### Playlist App

An app that uses spotify api where you can:
1. Check people's playlists
2. Upvote/Downvote
3. Add your own playlist


#### goal:
provide an environment where people can share/discover their musical playlists, very useful in the workplace


#### use cases:

navigation:
playlists/ homepage
login/sign up

Homepage/not signed in
A list of random 10 playlists. 
Option to Sign up/Login, which takes you to a page with both forms.

Log In/Sign up forms on one page
Both options if successful redirect you to the home page, but now logged in and showing the playlists you have and the playlists you have added.

Homepage/logged in
A user can now see their personalized content, with their own playlists and the ones they added.

#### Templates
##### templates/user
Login/Signup: provide secure way for user to login/signup. Redirects to playlists.html


##### templates/playlists
playlists.html : list of playlist, if else statement that distinguishes if user is signed in or not.
A search field that searches new playlist
Ability to add new playlists

base.html  
404.html

#### Add a song and it will suggest you 3 related songs. Add a song to playlist.


#### Technologies Used

Flask



