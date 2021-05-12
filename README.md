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
The purpose of this program is to take JSON input files and translate
any units of memory to an integer of bytes. The translated result
will be JSON output file with the naming convention
"part_four_output_##.json" with ## being the number corresponding
to the order the input files were read and translated.

### Run
    $ python3 convert_tasks.py -f <input-file>, <input-file>, ...

### Command-line options
    -f, --files: Specify the input file(s).

### Input file format
Each input file should have one or more tasks. This program will
scan the values inside each task. Each "task" will have 5 features:
```
{
    "TASK01": {
    "cpu": "#_of_CPUs_needed_by_task",
    "mem": "memory_size",
    "disk": "memory_size",
    "time": "ammount_of_time_to_complete_task",
    "relies_on": "TASK##"
    },
    ...
}
```
The program will translate every "memory_size" value to bytes.

## Part Five (unfinished)
Note: This program is unfinished.

The purpose of this program is to find the shortest possible
runtime given a JSON input file of tasks. Only one 16 core
computer is given to run these tasks.

### Thought process
First, create a Graph of all the tasks with dependencies.
Run a Depth-First Search algorithm on the Graph to determine
what level a certain task is.

Then, push all the parent (first-level) tasks onto a priority 
queue ordered by longest time first.

Iterate through the priority queue. For each task t, create a
sublist of tasks with a CPU cost of the complement of t's
CPU cost. For instance, if t had a CPU cost of 5, create a
sublist of tasks with a CPU cost of (16 - 5) or lower.

Execute as many tasks in t's sublist as CPU limitations
(16 cores) allow. Record the maximum time taken to execute
one of these tasks, including t.

Remove t and all executed tasks from the priority queue. 

Now, all parent tasks have been executed. Push the next level 
tasks onto the priority queue and repeat the procedure above.

This program is not perfect because of the possibility that the
CPU is not fully utilized at all times.

### Run
    $ python3 find_shortest_runtime.py -f <input-file>

### Commands-line options
    -f, --file: Specify the input file.

### Input file format
Each input file should have one or more tasks. Each "task" will
have at least 2 features with an optional "relies_on" feature:
```
{
    "TASK00": {
        "cpu": 13,
        "time": 851
    },
    "TASK01": {
        "cpu": 9,
        "time": 506,
        "relies_on": 13
    },
    ...
}
```