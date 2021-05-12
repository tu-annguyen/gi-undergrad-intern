import sys, getopt, json

def main(argv):
    infile = None 

    print(argv)

    # Check for one input file as a command-line argument.
    if len(argv) != 2:
        print('Invalid command. Usage: find_shortest_runtime.py -f <input-file>')
        sys.exit(2)

    # Get command-line arguments for input file. Store in opts, args.
    try:
        opt, arg = getopt.gnu_getopt(argv, 'f', ['file='])
    except getopt.GetoptError:
        print('Invalid command. Usage: find_shortest_runtime.py -f <input-file>')
        sys.exit(2)

    # Set infile to input file specified in command-line argument.
    infile = arg

    open(infile, 'r')

    tasks = json.load(infile)

    # for task in tasks:
        # if tasks[task].has_key('relies_on'):
            # g.addEdge(task, tasks[task]['relies_on'], tasks[task]['time'])

    infile.close()

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])