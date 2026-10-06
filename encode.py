import random, string
import numpy as np
from pathlib import Path
from PIL import Image
from helpers.message import PRINT_ERROR, PRINT_SUCCESS


def random_delimiter():
    random.seed()
    ascii = string.ascii_letters + string.punctuation + string.digits
    delimiter = ""
    for i in range(0, 10):
        random_index = random.randint(0, (len(ascii) - 1))
        delimiter += ascii[random_index]
    return delimiter


def destination_name(source):
    source = Path(source)
    return source.parent / f"enc.{source.name}"


def encode_rgb(image, message, delimiter):
    pixels = np.array(image)

    # Extract RGB channels and make an explicit writable copy.
    rgb = pixels[:, :, :3].copy().reshape(-1)

    message_bytes = (message + delimiter).encode("utf-8")
    bits = np.fromiter(
        (bit for byte in message_bytes for bit in format(byte, "08b")),
        dtype=np.uint8
    )

    if len(bits) > rgb.size:
        raise PRINT_ERROR(ValueError(f"Message is too large. Maximum capacity: {rgb.size // 8} bytes."))

    rgb[:len(bits)] = (rgb[:len(bits)] & 0xFE) | bits

    # Put modified RGB data back into the original image array.
    pixels[:, :, :3] = rgb.reshape(pixels[:, :, :3].shape)

    return pixels


def encode_l(image, message, delimiter):
    pixels = np.array(image)

    # Flatten grayscale pixels into a 1D array.
    # gray = pixels[:, :, :2].copy().reshape(-1)
    if pixels.ndim == 2:  # L
        gray = pixels.reshape(-1)
    else:  # LA
        gray = pixels[:, :, 0].copy().reshape(-1)
    
    message_bytes = (message + delimiter).encode("utf-8")

    bits = np.fromiter(
        (bit for byte in message_bytes for bit in format(byte, "08b")),
        dtype=np.uint8
    )
    if len(bits) > gray.size:
        raise PRINT_ERROR(ValueError(f"Message is too large. Maximum capacity: {gray.size // 8} bytes."))

    # Replace LSBs with message bits.
    gray[:len(bits)] = (gray[:len(bits)] & 0xFE) | bits

    # Put modified L/A data back into the original image array.
    # pixels[:, :, :2] = gray.reshape(pixels[:, :, :2].shape)
    if pixels.ndim == 3:  # LA
        pixels[:, :, 0] = gray.reshape(pixels[:, :, 0].shape)
    
    return pixels


def encoding_mode(image, message, delimiter):
    if image.mode in ("RGB", "RGBA"):
        return encode_rgb(image, message, delimiter)
    elif image.mode == "L":
        return encode_l(image, message, delimiter)
    else:
        raise PRINT_ERROR(ValueError(f"Unsupported image mode: {image.mode}"))


def encode(input_file, message, delimiter, output_file):
    try:
        image = Image.open(input_file)
    except Exception as e:
        print(f"Unable to open file: {e}")
        return False

    if delimiter is None:
        delimiter = random_delimiter()
        PRINT_SUCCESS(f"This is Your new random delimiter: {delimiter}")

    pixels = encoding_mode(image, message, delimiter)

    ## save image
    try:
        encoded_image = Image.fromarray(pixels, image.mode)
        if output_file == None:
            output_file = destination_name(input_file)
        encoded_image.save(output_file)
        PRINT_SUCCESS(f"Image saved to {output_file}")
    except Exception as e:
        PRINT_ERROR(f"Unable to save encoded image: {e}")
        return False

    return True
