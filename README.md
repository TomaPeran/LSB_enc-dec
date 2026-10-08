# LSB Steganography

A simple Python tool for hiding and extracting text messages inside images using Least Significant Bit (LSB) steganography.

## Features

- Encode text messages into images
- Decode hidden messages from images
- Supports:
  - RGB
  - RGBA
  - L (grayscale)
- Custom delimiters
- Random delimiter generation
- Command-line interface
- NumPy-based bit manipulation

## Installation

Clone the repository:

    git clone <repository-url>
    cd LSB_Enc_Dec

Install dependencies:

    pip install -r requirements.txt

## Usage

### Encode

    python3 main.py encode -i input.png -m "Hello world" -c test -o output.png

Arguments:

    -i, --input-file
        Image to encode.

    -m, --message
        Message to hide inside the image.

    -c, --custom-delimiter
        Delimiter used to mark the end of the message.

    -o, --output-file
        Output image. If omitted, an output filename is generated automatically.

### Decode

    python3 main.py decode -i output.png -p test

Arguments:

    -i, --input-file
        Image containing the hidden message.

    -p, --passphrase
        Delimiter used when encoding the message.

## Example

Encode:

    python3 main.py encode \
        -i flower.png \
        -m "Hello world" \
        -c test \
        -o encoded.png

Decode:

    python3 main.py decode \
        -i encoded.png \
        -p test

Output:

    Hello world

## Supported Image Modes

    RGB      Yes
    RGBA     Yes
    L        Yes
    LA       Yes
    Other    To be added

For RGBA images, the alpha channel is not modified.

## Image Formats

LSB steganography requires the pixel values to remain unchanged.
Use lossless formats such as PNG or BMP for the encoded output.
JPEG should NOT be used as the output format because JPEG compression can modify the pixel values and destroy the hidden message.
A JPEG can still be used as the input image if the encoded image is saved as a lossless format (for example, JPEG input and PNG output).

## How It Works

The message is converted to UTF-8 bytes and then into individual bits.
These bits are stored in the least significant bit of image pixel values.

Example:

    Original pixel:  10110110
    Message bit:            1
    Encoded pixel:   10110111

Only the least significant bit is changed, so the visual difference is negligible.
For RGB and RGBA images, the red, green, and blue channels are used.
For RGBA images, the alpha channel is left untouched.
For L images, the least significant bit of each grayscale pixel is used.

## Dependencies

- Python 3
- NumPy
- Pillow

Install dependencies with:

    pip install -r requirements.txt

## Project Structure

    ├── decode.py       -> Encoding functionality
    ├── encode.py       -> Decoding functionality
    ├── helpers
    │   ├── message.py
    │   └── parser.py
    ├── main.py         -> Command-line interface
    ├── README.md
    └── requirements.txt
    
## TODO:
- [ ] Add encryption (e.g. AES-GCM) before embedding the message.
- [ ] Add tests for encoding/decoding, including Unicode and edge cases.
- [ ] Improve error handling for invalid images and messages that exceed image capacity.
- [ ] Add support for embedding arbitrary binary files, not only text messages.
- [ ] Improve the embedding algorithm by using pseudorandom pixel positions derived from a key.


## Disclaimer

This project is an educational implementation of LSB steganography.
It is intended for learning about image manipulation, binary data, NumPy, and steganography.

