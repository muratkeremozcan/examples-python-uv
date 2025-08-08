playlist_list = [
    1,
    "Blinding Lights",
    "The Weeknd",
    2,
    "One Dance",
    "Drake",
    3,
    "Uptown Funk",
    "Mark Ronson",
    4,
    "Closer",
    "The Chainsmokers",
    5,
    "One Kiss",
    "Calvin Harris",
    6,
    "Mr. Brightside",
    "The Killers",
    7,
    "Echo",
    "Coldplay",
]


# covert into a dictionary
# range(start, stop, step)
playlist = {
    playlist_list[i + 2]: playlist_list[i + 1] for i in range(0, len(playlist_list), 3)
}

print(playlist)

# just print the first 2 elements
# print(playlist := {playlist_list[i + 2]: playlist_list[i + 1] for i in range(0, 6, 3)})

# Print the song by Coldplay
print(playlist["Coldplay"])

# Add a new song Usher Yeah!
playlist["Usher"] = "Yeah!"

# Print the song names in the playlist
print(playlist.values())
