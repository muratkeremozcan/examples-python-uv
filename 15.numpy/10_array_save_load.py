import numpy as np

# Key takeaways (save/load arrays):
# - .npy is NumPy's fast, compact format for arrays.
# - np.save/np.load work with binary files ("wb" / "rb").
# - RGB images are 3D arrays: (rows, cols, channels).
# - np.where can replace values (e.g., change a background).
# - help(np.unique) shows quick docs without leaving Python.

# Tiny RGB "image"
# (rows, cols, channels)
# Each pixel is [R, G, B], so the 3rd axis (index 2) is the color channel.
logo_rgb = np.array(
    [
        [[255, 0, 0], [255, 255, 0]],
        [[0, 0, 0], [255, 255, 255]],
    ],
    dtype=np.uint8,
)
# (2, 2, 3) → 2 rows, 2 columns, 3 channels (R,G,B).
# print(logo_rgb)
# [
#  [
#   [255   0   0]
#   [255 255   0]
#  ]
#  [
#   [  0   0   0]
#   [255 255 255]
#  ]
# ]

# Save and load a .npy file.
with open("15.numpy/logo.npy", "wb") as f:
    np.save(f, logo_rgb)

with open("15.numpy/logo.npy", "rb") as f:
    logo_loaded = np.load(f)

# Slice channels (R, G, B).
# logo_loaded[:, :, 0] → all rows, all cols, red channel
# logo_loaded[:, :, 1] → green channel
# logo_loaded[:, :, 2] → blue channel
red = logo_loaded[:, :, 0]
green = logo_loaded[:, :, 1]
blue = logo_loaded[:, :, 2]
# red   = [[255, 255],
#          [  0, 255]]

# green = [[  0, 255],
#          [  0, 255]]

# blue  = [[  0,   0],
#          [  0, 255]]
print(red[0], green[0], blue[0])
# [255 255] [  0 255] [0 0]

# Replace bright pixels (255) with 50 to darken the image.
dark_logo = np.where(logo_loaded == 255, 50, logo_loaded)

with open("15.numpy/dark_logo.npy", "wb") as f:
    np.save(f, dark_logo)

# Example docs lookup (commented to avoid printing a long help page).
# help(np.unique)
