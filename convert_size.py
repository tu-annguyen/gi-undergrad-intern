import sys
from convert import *

def main(argv):
    if len(argv) > 1:
        print('Invalid command. Usage: convert_size.py <byte-unit>')
        sys.exit(2)

    # str: String of the input value. Includes byte unit e.g. KiB, GB, TB.
    # val: Integer representation of input value. Stored in a string.
    # unit: Unit of bytes e.g. K, M, G. Stored in a string.
    # bi: Indicates whether or not the input value is a bibyte or not with the presence of 'i'.
    # byte: Stores the letter 'B.' Confirms the input value is a unit of bytes.
    str = argv[0] 
    try:
        val, unit, bi, byte = regex.search(str).groups() 
    except AttributeError:
        print('Invalid byte value. Refer to examples of correct byte values:\n- 400B\n- 40KB\n- 50MiB\nInput is not case sensitive.')
        sys.exit(2)

    val_converted = convert(val, unit, bi)
    print(val_converted)

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])