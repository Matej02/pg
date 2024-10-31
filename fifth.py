import sys

def read_header(file_name, header_length):
    try:
        with open(file_name, "rb") as f:
            return f.read(header_length)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Cannot read file '{file_name}'.")
        sys.exit(1)


def is_jpeg(header):
    # Kontroluje JPEG podle standardního podpisu 0xFFD8 na začátku a 0xFFD9 na konci
    return header[:2] == b'\xff\xd8' and header[-2:] == b'\xff\xd9'


def is_gif(header):
    # Kontroluje GIF podle podpisu GIF87a nebo GIF89a na začátku
    return header[:6] in (b'GIF87a', b'GIF89a')


def is_png(header):
    # Kontroluje PNG podle podpisu 0x89504E470D0A1A0A na začátku
    return header[:8] == b'\x89PNG\r\n\x1a\n'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python fifth.py <path/to/image>")
        sys.exit(1)

    file_name = sys.argv[1]
    header_length = 8  # Nastaví délku hlavičky pro PNG (nejdelší z formátů)

    header = read_header(file_name, header_length)

    if is_jpeg(header):
        print(f"{file_name} is a JPEG image.")
    elif is_gif(header):
        print(f"{file_name} is a GIF image.")
    elif is_png(header):
        print(f"{file_name} is a PNG image.")
    else:
        print(f"{file_name} is of an unknown or unsupported image type.")
