import numpy as np

# Key takeaways (array acrobatics):
# - np.flip reverses element order along axes (data augmentation).
# - axis lets you flip specific axes; a tuple flips multiple axes.
# - np.transpose reorders axes without changing element order within axes.

logo_rgb = np.array(
    [
        [[255, 0, 0], [255, 255, 0]],
        [[0, 0, 0], [255, 255, 255]],
    ],
    dtype=np.uint8,
)
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


# Flip all axes (rows, cols, and channels).
print(np.flip(logo_rgb))
# [
#   [
#    [255 255 255]
#    [  0   0   0]
#   ]
#   [
#    [  0 255 255]
#    [  0   0 255]
#   ]
# ]

# Flip only rows (axis 0) - mirror vertically (top/bottom).
print(np.flip(logo_rgb, axis=0))
# [
#   [
#     [  0   0   0]
#     [255 255 255]
#   ]
#   [
#     [255   0   0]
#     [255 255   0]
#   ]
# ]

# Flip only columns (axis 1) - mirror horizontally (left/right).
print(np.flip(logo_rgb, axis=1))
# [
#   [
#     [255 255   0]
#     [255   0   0]
#   ]
#   [
#     [255 255 255]
#     [  0   0   0]
#   ]
# ]

# Flip only channels (axis 2) - swap RGB order (not a spatial mirror).
print(np.flip(logo_rgb, axis=2))
# [
#   [
#    [  0   0 255]
#    [  0 255 255]
#   ]
#   [
#    [  0   0   0]
#    [255 255 255]
#   ]
# ]


# Flip rows + cols, keep channels the same.
print(np.flip(logo_rgb, axis=(0, 1)))
# [
#   [
#     [255 255 255]
#     [  0   0   0]
#   ]
#   [
#     [255 255   0]
#     [255   0   0]
#   ]
# ]


# Transpose: swap rows and columns, keep channels last.
print(np.transpose(logo_rgb, axes=(1, 0, 2)))
# [
#   [
#    [255   0   0]
#    [  0   0   0]
#   ]
#   [
#     [255 255   0]
#     [255 255 255]
#   ]
# ]
