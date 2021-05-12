# UC Santa Cruz Genomics Institute Undergraduate Programming Assessment

## Part One
The difference between a gigabyte (GB) and a gibibyte (GiB) is the
amount of memory each represents. 1 GB = 1,000,000 B. Meanwhile,
1 GiB = 1,073,741,824. These two units are based on different
powers. The former is based on powers of 10 while the latter is
based on powers of 2. 

## Part Two
Binary architecure of computers allows for the units based on
powers of 2 (e.g. GiB) most practical. However, the metric
prefixes such as kilo, mega, and giga arose due to convenience,
because 1024 is approximate to 1000. 

Source: https://en.wikipedia.org/wiki/Byte#History_of_the_conflicting_definitions

## Part Three
The purpose of this program is to handle the translation from units
of memory to an integer of bytes with the following units:
    byte (B),
    kilobyte (KB),
    megabyte (MB),
    gigabyte (GB),
    terabyte (TB),
    petabyte (PB),
    exabyte (EB),
    zettabyte (ZB),
    yottabyte (YB),
    kibibyte (KiB),
    mebibyte (MiB),
    gibibyte (GiB),
    tebibyte (TiB),
    pebibyte (PiB),
    exbibyte (EiB),
    zebibyte (ZiB),
    and yobibyte (YiB).
This program is not case sensitive (e.g. 50MiB == 50mib == 50MIB).

### Run
    $ python3 convert_size.py <byte-unit>

## Part Four
The purpose of this program is to take .json input files and translate
any units of memory to an integer of bytes. The translated result
will be .json output file with the naming convention
"part_four_output_XX.json" with XX being the number corresponding
to the order the input files were read and translated.

### Run
    $ python3 convert_tasks.py -f <input-file>, <input-file>, ...

### Command-line options
    -f, --file: Specify the input file(s).

### Input file format
This program is built to accept json input files of similar format
to this:
    {
    "TASK01": {
    "cpu": "4",
    "mem": "5GB",
    "disk": "4Gib",
    "time": 135,
    "relies_on": "TASK03"}
    }