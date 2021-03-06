import sys, getopt, json
from convert import *

def main(argv):
    infiles = []
    outfiles = []

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
            outfile = 'part_four_output_0' # '0' prefixing.

        outfile += str(outfile_num) + '.json'
        outfiles.append(outfile)

        outfile_num += 1

    # Iterate through infiles and outfiles simultaneously.
    for ifile, ofile in zip(infiles, outfiles):
        infile = open(ifile, 'r')
        outfile = open(ofile, 'w')
       
        dict = json.load(infile) # Parse json into a dictionary.

        # Iterate through the dictionary.
        for key in dict:
            for k in dict[key]:
                val, unit, bi, = None, None, None

                # Scan dictionary of values for byte units. 
                try:
                    val, unit, bi = regex.search(dict[key][k]).groups() 
                except (AttributeError, TypeError):
                    pass

                # Convert the byte unit into its byte representation and overwrite the conversion into dict.
                if val is not None and val != '':
                    val_converted = convert(val, unit, bi)
                    dict[key][k] = str(val_converted)

        outfile.write(json.dumps(dict, indent = 4)) # Write translated json dict into outfile.
        
        infile.close()
        outfile.close()
    
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])