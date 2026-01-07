import pandas as pd

# Key takeaways (verify integrity):
# - merge(validate=...) checks expected join shape (one_to_one, one_to_many, many_to_one, many_to_many).
# - concat(verify_integrity=True) fails if index values overlap.
# - Errors signal data issues (duplicates) to fix before analysis.

# Example: validate a one-to-one merge.
tracks = pd.DataFrame(
    {
        "tid": [1, 2, 3],
        "title": ["Intro", "Pulse", "Echo"],
    }
)
# print(tracks)
#    tid  title
# 0    1  Intro
# 1    2  Pulse
# 2    3   Echo


specs = pd.DataFrame(
    {
        "tid": [1, 2, 2],
        "bitrate": [320, 256, 256],
    }
)
# print(specs)
# 	 tid   bitrate
# 0    1      320
# 1    2      256
# 2    2      256

# This should be one-to-one, but specs has a duplicate tid.
try:
    tracks_specs = tracks.merge(specs, on="tid", validate="one_to_one")
except pd.errors.MergeError as exc:
    print(exc)
    print()

# one-to-many-would work
tracks_specs = tracks.merge(specs, on="tid", validate="one_to_many")
# print(tracks_specs)
#    tid  title  bitrate
# 0    1  Intro      320
# 1    2  Pulse      256
# 2    2  Pulse      256

################
# One-to-many merge passes validation.
albums = pd.DataFrame(
    {
        "album_id": [10, 10, 20],
        "tid": [1, 2, 3],
        "album_name": ["Alpha", "Alpha", "Beta"],
    }
)
print(albums)
#    album_id  tid album_name
# 0        10    1      Alpha
# 1        10    2      Alpha
# 2        20    3       Beta

tracks_albums = albums.merge(tracks, on="tid", validate="one_to_many")
print(tracks_albums)
#    album_id  tid album_name  title
# 0        10    1      Alpha  Intro
# 1        10    2      Alpha  Pulse
# 2        20    3       Beta   Echo

# ########################
# concat(verify_integrity=True)
# Example: verify integrity when concatenating on index.

inv_feb = pd.DataFrame(
    {
        "invoice_id": [8, 9],
        "amount": [30, 45],
    }
).set_index("invoice_id")
# print(inv_feb)
# invoice_id
# 8     30
# 9     45

inv_mar = pd.DataFrame(
    {
        "invoice_id": [9, 10],
        "amount": [40, 55],
    }
).set_index("invoice_id")
# print(inv_mar)
# invoice_id
# 9     40
# 10    55

# verify_integrity=True raises when index values overlap.
try:
    inv_bad = pd.concat([inv_feb, inv_mar], verify_integrity=True)
except ValueError as exc:
    print(exc)

# Default behavior allows duplicate index values.
inv_ok = pd.concat([inv_feb, inv_mar])
print(inv_ok)
