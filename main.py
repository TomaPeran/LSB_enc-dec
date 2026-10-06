from encode import encode
from decode import decode
from helpers.parser import args
from helpers.message import PRINT_ERROR, PRINT_SUCCESS


if __name__ == "__main__":
    ## supports png input and png output
    ## supports jpeg input and png output
    ## supports bmp and greyscale input and output
    ## TODO: add exception value when entering jpg/jpeg image, it has to have output in png format
    if args.action == "encode":
        result = encode(args.input_file, args.message, args.custom_delimiter, args.output_file)
    elif args.action == "decode":
        result = decode(args.input_file, args.passphrase)
    else:
        PRINT_ERROR("No such option")

    PRINT_SUCCESS(f"Operation successfully executed") if result else PRINT_ERROR(f"Operation failed")
