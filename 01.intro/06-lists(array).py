# Create the playlist variable
playlist = [
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
]

# Print the list
print(playlist)

# Find the name of the second song, which is the fifth element, in the playlist,
# and print the value.
print(playlist[4])

# Print the name of the artist for the final song in the playlist
print(playlist[-1])

# Print every song name in the playlist.
print(playlist[1::3])

# JS: playlist.filter((_, index) => index % 3 === 1);
