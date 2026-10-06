from argparse import ArgumentParser

parser = ArgumentParser(description="Encode/decode data with LSB")
subparsers = parser.add_subparsers(dest="action", required=True)

## Encode
encode_parser = subparsers.add_parser("encode", help="Encode a message into an image")
encode_parser.add_argument("-i", "--input-file", type=str, required=True, help="Input image file to encode/decode.")
encode_parser.add_argument("-m", "--message", type=str, required=True, help="Message to encode inside the image.")
encode_parser.add_argument("-c", "--custom-delimiter", type=str,required=False, help="Set a custom delimiter/passphrase when encoding.")
encode_parser.add_argument("-o", "--output-file", type=str, required=False, help="Output file to write the encoded image.")

## Decode
decode_parser = subparsers.add_parser("decode", help="Decode a message from an image")
decode_parser.add_argument("-i", "--input-file", type=str, required=True, help="Input image file to encode/decode.")
decode_parser.add_argument("-p", "--passphrase", type=str, required=True, help="Passphrase for decoding the image.")
args = parser.parse_args()