import sys
from PIL import Image
import numpy as np

def main():
    if len(sys.argv) != 3:
        print("Usage: python bmp2h.py <input.bmp> <output.h>")
        sys.exit(1)
    
    bmp_path = sys.argv[1]
    output_path = sys.argv[2]
    
    try:
        # Open the image and convert it to grayscale (1-bit color)
        img = Image.open(bmp_path).convert("1")
    except IOError:
        print(f"Error: Unable to open image file '{bmp_path}'.")
        sys.exit(1)
    
    # Get the size of the image
    width, height = img.size
    
    # Convert the image to a NumPy array
    bitmap = np.array(img)
    
    # Convert the bitmap to a 1D array of bits
    bitmap_bits = np.packbits(bitmap, axis=-1)
    
    # Format the array as C code
    output = []
    for byte in bitmap_bits.flatten():
        output.append(f"0x{byte:02X}")
    
    # Create the C array
    c_array = f"const uint8_t icon_data[] PROGMEM = {{\n    {', '.join(output)}\n}};\n"
    
    try:
        # Write the array to the output file
        with open(output_path, "w") as file:
            file.write(c_array)
        print(f"C array created and saved to '{output_path}'.")
    except IOError:
        print(f"Error: Unable to write to file '{output_path}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()
