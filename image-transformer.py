from PIL import Image
import numpy as np

img = Image.open("images/logo.png").convert("RGBA")
arr = np.array(img)

# Detect white background
bg_threshold = 250
is_bg = (arr[...,0] >= bg_threshold) & \
        (arr[...,1] >= bg_threshold) & \
        (arr[...,2] >= bg_threshold)

# Make background transparent
arr[is_bg, 3] = 0

# Set line color
arr[~is_bg] = [223, 240, 255, 255]

out = Image.fromarray(arr, "RGBA")
out.save("logo_transparent.png")
