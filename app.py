from flask import Flask, request, redirect, g, render_template, session
from spotify_requests import spotify

app = Flask(__name__)
app.secret_key = 'some key for session'


