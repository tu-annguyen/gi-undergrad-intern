import sys
from convert import *

def main(argv):
    # Check for sufficient command-line arguments.
    if len(argv) > 1:
        print('Invalid command. Usage: convert_size.py <byte-unit>')
        sys.exit(2)

    # str: String of the input value. Includes byte unit e.g. KiB, GB, TB.
    str = argv[0] 

    # Scan the input with regex and store val, unit, and bi accordingly.
    try:
        val, unit, bi = regex.search(str).groups() 
    except AttributeError:
        print('Invalid byte value. Refer to examples of correct byte values:\n- 400B\n- 40KB\n- 50MiB\nInput is not case sensitive.')
        sys.exit(2)

    # Translate and print the byte representation using val, unit, and bi. 
    val_converted = convert(val, unit, bi)
    print(val_converted)

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])