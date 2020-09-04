
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


####
Api
find base url for all endpoints

#### Technologies Used

Flask



notes:
Capstone Project: Finding New Music

What will the app do?
This app will use spotify api that will enable you to search for artists and playlists.  The goal is to find new music using spotify’s api.

It will have 2 main pages:  a Homepage and a profile page. It will allow users to sign up/login and log out.

Authorization routes:

/login: render login.html
/login POST it will attempt to login with users credentials, if successful, it will go to the profile page, if unsuccessful it will take you back to login page

/sign up it will render signup.html
/sign up POST it will attempt to sign up.
If user already exists, it will inform the user that it already exists, and it will redirect to login page
if user does not exist, it will add new user to database and redirect to profile page so he can start searching new songs/playlists

/logout if will return app to initial state, so that it won’t be associated with any user, and then redirect app to index.html

Main Routes

/homepage render index.html it will show routes to login or sign up and it will describe the app’s functionalities
/profile page render profile.html it will show users name. It will have a search bar where users can search for artists or playlists that the user can add to their profile.

How the user interacts with the webpage?

Model
User
id
email
password
Name




Connecting to Spotify

To connect our app to spotify, we are going to work from a different file: spotify_requests.py. On this file we will create a class SpotifyAPI(object)

We will then go to their developer site and create an app on their site that will have a client ID and client secret.

Step 1: Get token
With these two (client ID and client secret), one will be able to create a token to be able to authenticate with spotify api. For this, you will need the requests library from python.
We use that token to make requests in the future. That token expires at some point. So it will be the equivalent of logging in to a session and staying logged in.

Authorization flows

On their website, there are 3 types of authorization flows.
We need to look into one of the authorization flows in Spotify “Client Credentials Flow” that uses the Client ID and Secret Key to get the Access Token.

token_url : https://accounts.spotify.com/api/token
The method is POST.
Parameters that are required:
token_data:
grant_type: client_credentials
 
Token_header:
base 64 encoded string (this step will require adding a base64 library to encode string

So, the request will be:

response = requests.post(token_url, data= token_data, headers=token_headers)

This response will give us an access token.



Step Two: Create a search using spotify api

endpoint: https://api.spotify.com/v1/search
method: GET
Parameters:
required parameter:Authorization (done on step 1)
data:  q’ for query “type”: “artist”

response = requests.get(endpoint, data=data, headers=headers)

What will the user do with their search results?
Save them, add to playlist.

Can the user have more than one playlist?

Make a new playlist
A user has multiple playlists
A playlist has multiple songs





