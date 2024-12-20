from PIL import Image
import numpy as np

# Replace with your Bitmap Array
bitmap = [
	0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x0f,0x00,0x01,0xff,0x00,0x7f,0xff,0x01,0xff,0xff,0x01,0xff,0xff,0x01,0xff,0xff,
	0x01,0xff,0xff,0x01,0xff,0xc3,0x01,0xf8,0x03,0x01,0x80,0x03,0x01,0x80,0x03,0x01,0x80,0x03,0x01,0x80,0x03,0x01,0x80,0x03,
	0x01,0x80,0x03,0x01,0x80,0x03,0x01,0x80,0x03,0x01,0x80,0x03,0x01,0x80,0x0f,0x01,0x80,0x7f,0x01,0x80,0xff,0x0f,0x81,0xff,
	0x7f,0x81,0xff,0xff,0x80,0xfe,0xff,0x80,0xfc,0xff,0x00,0x00,0xff,0x00,0x00,0x7e,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00
]

# Replace with your dimensions
width = 24
height = 32

# Convert bitmap array to binary
bitmap_bits = np.unpackbits(np.array(bitmap, dtype=np.uint8)).reshape(-1, width)

# Create an image (invert colors for OLED: 1=white, 0=black)
bitmap_image = (1 - bitmap_bits) * 255
image = Image.fromarray(bitmap_image.astype(np.uint8), mode='L')

# Save and display the image
image.save("output.png")
image.show()
