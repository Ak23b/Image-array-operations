import numpy as np

# Create a fake grayscale imge
img = np.random.randint(0,256,(5,5),dtype=np.uint8)
print("Original Image: \n",img)

# Detect pixels greater than 200
bright_pixels = img[img>200]
print("Pixels greater than 200:\n",bright_pixels)

# Set all pixels less than 50 to 0(darken)
img[img<50] = 0
print("Image after darkening pixels less than 50:\n ",img)

# Create a mask for pixels between 100 and 150
mask = (img >= 100) & (img <= 150)
print("Mask for pixels between 100 and 150:\n",mask)

# Highlight these mask pixels by setting them to 255
img[mask] = 255
print("Image after highlighting pixels between 100 and 150:\n",img)

