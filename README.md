# Moodify - Spotify Playlist Generator

Moodify is a simple Python script that helps you create a Spotify playlist based on your current mood. It utilizes the Spotify API and the Spotipy library for Python to create a new private playlist and populate it with tracks that match your mood. The script also uses the dotenv library to load your Spotify API credentials securely from an environment file.

## Prerequisites

Before you can use Moodify, make sure you have the following prerequisites in place:

- A Spotify Developer Account: You need to create a Spotify Developer application and obtain the `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` credentials.
- Python 3.x: Make sure you have Python installed on your system.
- Spotipy Library: You can install this library via pip with `pip install spotipy`.
- dotenv Library: Install dotenv with `pip install python-dotenv`.

## Installation

1. Clone or download the Moodify repository to your local machine.

2. Create a file named `.env` in the same directory as the Moodify script. Add your Spotify API credentials to this file:

   ```shell
   SPOTIPY_CLIENT_ID=your_client_id
   SPOTIPY_CLIENT_SECRET=your_client_secret
Update the SPOTIPY_REDIRECT_URI in the script if needed. By default, it's set to http://localhost:8888/callback.


## Usage

1. Open a terminal and navigate to the directory containing the Moodify script.

2. Run the script by executing the following command:

   ```shell
   python moodify.py

3. Follow the instructions on the screen to create a new playlist and populate it with tracks that match your mood.

## Run

```shell
python main.py
```

## Acknowledgements
This was created by abhiram2504