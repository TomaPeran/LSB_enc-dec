import numpy as np
from PIL import Image
from helpers.message import PRINT_ERROR, PRINT_SUCCESS, PRINT_MESSAGE


def decode_rgb(image, delimiter):
    pixels = np.array(image)

    # Use only RGB channels, leaving alpha untouched
    rgb = pixels[:, :, :3].reshape(-1)

    # Extract the LSB from every RGB channel
    bits = rgb & 1

    # Convert bits into bytes
    bits = bits[:len(bits) // 8 * 8]
    byte_bits = bits.reshape(-1, 8)
    bytes_array = np.packbits(byte_bits)

    # Convert bytes to UTF-8 text
    data = bytes_array.tobytes()
    delimiter_bytes = delimiter.encode("utf-8")

    # Find the delimiter
    delimiter_index = data.find(delimiter_bytes)
    if delimiter_index == -1:
        raise PRINT_ERROR(ValueError("No message found or incorrect delimiter."))

    return data[:delimiter_index].decode("utf-8")


def decode_l(image, delimiter):
    pixels = np.array(image)

    # Flatten grayscale pixels into a 1D array
    gray = pixels[:, :, :0].reshape(-1)

    # Extract the LSB from every L/A channel
    bits = gray & 1

    # Convert bits into bytes
    bits = bits[:len(bits) // 8 * 8]
    byte_bits = bits.reshape(-1, 8)
    bytes_array = np.packbits(byte_bits)

    # Convert bytes to UTF-8 text
    data = bytes_array.tobytes()
    delimiter_bytes = delimiter.encode("utf-8")

    # Find the delimiter
    delimiter_index = data.find(delimiter_bytes)
    if delimiter_index == -1:
        raise PRINT_ERROR(ValueError("No message found or incorrect delimiter."))

    return data[:delimiter_index].decode("utf-8")


def decoding_mode(image, delimiter):
    if image.mode in ("RGB", "RGBA"):
        return decode_rgb(image, delimiter)
    elif image.mode == "L":
        return decode_l(image, delimiter)
    else:
        raise PRINT_ERROR(ValueError(f"Unsupported image mode: {image.mode}"))


def decode(input_file, delimiter):
    try:
        image = Image.open(input_file)
    except Exception as e:
        PRINT_ERROR((f"Unable to open file: {e}"))
        return False

    if delimiter is None:
        PRINT_ERROR("Delimiter is required for decoding.")
        return False

    try:
        message = decoding_mode(image, delimiter)
    except Exception as e:
        PRINT_ERROR(f"Unable to decode image: {e}")
        return False

    PRINT_MESSAGE(message)
    return True
