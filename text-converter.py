import sys
import base64

class TextConverter:
    def __init__(self, text):
        self.text = text

    def convert_to_binary(self):
        binary_value = "".join(format(ord(char), "08b") for char in self.text)
        return binary_value

    def convert_to_octal(self):
        octal_value = " ".join(format(ord(char), "03o") for char in self.text)
        return octal_value

    def convert_to_decimal(self):
        decimal_value = " ".join(str(ord(char)) for char in self.text)
        return decimal_value

    def convert_to_hex(self):
        hex_value = " ".join(format(ord(char), "02X") for char in self.text)
        return hex_value

    def convert_to_base64(self):
        encoded_text = base64.b64encode(self.text.encode()).decode()
        return encoded_text


def print_help():
    help_text = """
Usage: py text-converter [Option] text [Option]

Convert text to various representations.

Options:
  -a, --ascii     Convert to ASCII
  -b, --binary    Convert to binary
  -o, --octal     Convert to octal
  -d, --decimal   Convert to decimal
  -h, --hex       Convert to hexadecimal
  -b64, --base64  Convert to base64
"""
    print(help_text)


if __name__ == "__main__":
    args = sys.argv[1:]

    if not args or args[0] == "--help":
        print_help()
        sys.exit()

    if len(args) < 3:
        print("Invalid number of arguments. Please check your syntax")
        print_help()
        sys.exit(1)

    option = args[0]
    text = args[1]
    conversion = args[2]

    text_converter = TextConverter(text)
    converted_text = ""
    
    try:
        match option:
            case "-a" | "--ascii":
                match conversion:
                    case "-a" | "--ascii":
                        converted_text = text
                    case "-b" | "--binary":
                        converted_text = text_converter.convert_to_binary()
                    case "-o" | "--octal":
                        converted_text = text_converter.convert_to_octal()
                    case "-d" | "--decimal":
                        converted_text = text_converter.convert_to_decimal()
                    case "-h" | "--hex":
                        converted_text = text_converter.convert_to_hex()
                    case "-b64" | "--base64":
                        converted_text = text_converter.convert_to_base64()
                    case _:
                        print("Invalid conversion option.")
                        sys.exit(1)
            case "-b" | "--binary":
                match conversion:
                    case "-a" | "--ascii":
                        converted_text = "".join(chr(int(binary, 2)) for binary in text.split())
                    case "-b" | "--binary":
                        converted_text = text
                    case "-o" | "--octal":
                        converted_text = "".join(chr(int(binary, 2)) for binary in text.split())
                    case "-d" | "--decimal":
                        converted_text = str(int(text, 2))
                    case "-h" | "--hex":
                        converted_text = hex(int(text, 2))[2:]
                    case "-b64" | "--base64":
                        converted_text = "".join(chr(int(binary, 2)) for binary in text.split())
                    case _:
                        print("Invalid conversion option.")
                        sys.exit(1)
            case "-o" | "--octal":
                match conversion:
                    case "-a" | "--ascii":
                        converted_text = "".join(chr(int(octal, 8)) for octal in text.split())
                    case "-b" | "--binary":
                        converted_text = "".join(format(int(octal, 8), "03b") for octal in text.split())
                    case "-o" | "--octal":
                        converted_text = text
                    case "-d" | "--decimal":
                        converted_text = str(int(text, 8))
                    case "-h" | "--hex":
                        converted_text = "".join(format(int(octal, 8), "02X") for octal in text.split())
                    case "-b64" | "--base64":
                        binary_value = "".join(format(int(octal, 8), "03b") for octal in text.split())
                        converted_text = text_converter.convert_to_base64()
                    case _:
                        print("Invalid conversion option.")
                        sys.exit(1)
            case "-d" | "--decimal":
                match conversion:
                    case "-a" | "--ascii":
                        converted_text = "".join(chr(int(decimal)) for decimal in text.split())
                    case "-b" | "--binary":
                        converted_text = bin(int(text))[2:]
                    case "-o" | "--octal":
                        converted_text = oct(int(text))[2:]
                    case "-d" | "--decimal":
                        converted_text = text
                    case "-h" | "--hex":
                        converted_text = hex(int(text))[2:]
                    case "-b64" | "--base64":
                        converted_text = "".join(chr(int(decimal)) for decimal in text.split())
                    case _:
                        print("Invalid conversion option.")
                        sys.exit(1)
            case "-h" | "--hex":
                match conversion:
                    case "-a" | "--ascii":
                        converted_text = "".join(chr(int(hex_value, 16)) for hex_value in text.split())
                    case "-b" | "--binary":
                        converted_text = bin(int(text, 16))[2:]
                    case "-o" | "--octal":
                        converted_text = oct(int(text, 16))[2:]
                    case "-d" | "--decimal":
                        converted_text = str(int(text, 16))
                    case "-h" | "--hex":
                        converted_text = text
                    case "-b64" | "--base64":
                        converted_text = "".join(chr(int(hex_value, 16)) for hex_value in text.split())
                    case _:
                        print("Invalid conversion option.")
                        sys.exit(1)
            case "-b64" | "--base64":
                match conversion:
                    case "-a" | "--ascii":
                        converted_text = base64.b64decode(text).decode()
                    case "-b" | "--binary":
                        decoded_text = base64.b64decode(text)
                        binary_value = " ".join(format(byte, '08b') for byte in decoded_text)
                        converted_text = binary_value
                    case "-o" | "--octal":
                        decoded_text = base64.b64decode(text)
                        octal_value = " ".join(format(byte, '03o') for byte in decoded_text)
                        converted_text = octal_value
                    case "-d" | "--decimal":
                        decoded_text = base64.b64decode(text)
                        decimal_value = " ".join(str(byte) for byte in decoded_text)
                        converted_text = decimal_value
                    case "-h" | "--hex":
                        decoded_text = base64.b64decode(text)
                        hex_value = " ".join(format(byte, '02X') for byte in decoded_text)
                        converted_text = hex_value
                    case "-b64" | "--base64":
                        converted_text = text
                    case _:
                        print("Invalid conversion option.")
                        sys.exit(1)
            case _:
                print("Invalid option.")
                sys.exit(1)
    except ValueError:
        print_help()

    print(converted_text)
