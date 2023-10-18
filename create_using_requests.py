from flask import Flask, redirect, request
import random
import string

app = Flask(__name)

# Define your Spotify API credentials and callback URL
CLIENT_ID = 'YOUR_CLIENT_ID'
REDIRECT_URI = 'http://localhost:8888/callback'

# Define the route to initiate the Spotify authorization flow
@app.route('/login')
def login():
    state = generate_random_string(16)
    scope = 'user-read-private user-read-email'
    authorization_url = 'https://accounts.spotify.com/authorize?' + \
                       f'response_type=code&client_id={CLIENT_ID}&' + \
                       f'scope={scope}&redirect_uri={REDIRECT_URI}&state={state}'
    return redirect(authorization_url)

# Helper function to generate a random string
def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

if __name__ == '__main__':
    app.run(port=8888)
