playlist = {
    "title": "90's Hip-Hop",
    "author": "Spotify",
    "songs": [
        {"title": "Intergalactic", 
        "artist": ["Beastie Boys"], 
        "duration": 3.1},
        {"title": "Shimmy Shimmy Ya", 
        "artist": ["ODB"], 
        "duration": 2.1}
    ]
}

playlist_length = 0
for song in playlist['songs']:
    playlist_length += (song['duration'])
print(playlist_length)