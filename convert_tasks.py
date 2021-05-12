import sys, getopt, json
from convert import *

def main(argv):
    infiles = []
    outfiles = []

    print(argv)

    # Get command-line arguments for input files. Store in opts, args.
    try:
        opts, args = getopt.gnu_getopt(argv, 'f', ['files='])
    except getopt.GetoptError:
        print('Invalid command. Usage: convert_files.py -f <input-file>')
        sys.exit(2)

    # Add input and output files into infiles and outfiles lists, respectively.
    outfile_num = 0
    for arg in args:
        infiles.append(arg)

        outfile = 'part_four_output_'
        if outfile_num < 10:
            outfile = 'part_four_output_0' # 0 prefixing.

        outfile += str(outfile_num) + '.json'
        outfiles.append(outfile)

        outfile_num += 1

    print(infiles)
    print(outfiles)

    for file in infiles:
        infile = open(file, 'r')
        outfile = open(file, 'w')
        
        dict = json.loads(infile.read())

        for key, value in dict:
            try:
                val, unit, bi, byte = regex.search(value).groups() 
            except AttributeError:
                print('Invalid byte value. Refer to examples of correct byte values:\n- 400B\n- 40KB\n- 50MiB\nInput is not case sensitive.')
                sys.exit(2)

            if byte is not None:
                val_converted = convert(val, unit, bi)
                dict[value] = val_converted

        outfile.write(json.dumps(dict, indent = 4))
        
        infile.close()
        outfile.close()
    
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])