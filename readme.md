# bmp2x (bmp2img and bmp2h)

![GitHub License](https://img.shields.io/github/license/sleepy-dave/bmp2x?style=for-the-badge)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue?style=for-the-badge)

## Got a Bitmap-Array but no clue how to convert it? This Repo got you covered!

**bmp2x** is a handy repository with Python scripts to convert bitmap arrays into images or C-compatible code effortlessly.

## 📁 Repository Contents

- **`bmp2img.py`**: Converts a bitmap array to a PNG image.
- **`bmp2h.py`**: Converts a bitmap array to a C header file.

## 🚀 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sleepy-dave/bmp2x.git
   cd bmp2x
   ```

2. **Install Dependencies**

   ```bash
   pip install Pillow numpy
   ```

## 🛠️ Usage

### Convert Bitmap Array to Image (`bmp2img.py`)

Generates a PNG image from a predefined bitmap array.

**Before running the script, customize `bmp2img.py` by:**

1. **Replacing the Bitmap Array:**

   Open `bmp2img.py` and replace the `bitmap` list with your own bitmap data.

2. **Setting the Image Dimensions:**

   Update the `width` and `height` variables with your image's dimensions.

```bash
python bmp2img.py
```

*The image `output.png` will be saved and displayed.*

### Convert Bitmap Array to C Header (`bmp2h.py`)

Creates a C-compatible header file from a bitmap image.

```bash
python bmp2h.py input.bmp output.h
```

*Generates `output.h` containing the bitmap data.*

## 📦 Dependencies

- **Python 3.7+**
- **Pillow**
- **NumPy**

Install them using:

```bash
pip install Pillow numpy
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

---
