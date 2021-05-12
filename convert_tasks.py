import sys, getopt, json, itertools
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

    for ifile, ofile in zip(infiles, outfiles):
        infile = open(ifile, 'r')
        outfile = open(ofile, 'w')
       
        dict = json.load(infile)

        for key in dict:
            for k in dict[key]:
                val, unit, bi, byte = 0, None, None, None 
                
                try:
                    val, unit, bi, byte = regex.search(dict[key][k]).groups() 
                except (AttributeError, TypeError):
                    pass

                if byte is not None:
                    val_converted = convert(val, unit, bi)
                    dict[key][k] = val_converted

        outfile.write(json.dumps(dict, indent = 4))
        
        infile.close()
        outfile.close()
    
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])