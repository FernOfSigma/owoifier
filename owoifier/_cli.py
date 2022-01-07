"""Console entry point script."""

import argparse
import os.path as path
import sys

from . import __author__, __description__, __version__
from .owoifier import owoify


# Custom types for input
# ----------------------

def file(file_path):
    """Argument must be an existing file."""
    if path.isfile(file_path):
        file_path = path.expanduser(file_path)
        file_path = path.expandvars(file_path)
        return path.normpath(file_path)
    raise argparse.ArgumentTypeError(f"{file_path} is not a file.")

def chance(number):
    """Argument must lie within 0.0 and 1.0."""
    number = float(number)
    if 0.0 <= number <= 1.0:
        return number
    raise argparse.ArgumentTypeError("Chance must be within 0 and 1.")


# Parser configuration
# --------------------

parser = argparse.ArgumentParser(
    description=__description__,
    epilog=f"Written by {__author__}.",
    add_help=False
)

# Mutually exclusive argument group for input types
exclusive = parser.add_mutually_exclusive_group()

exclusive.add_argument(
    "-i", "--input-file",
    metavar="FILE", type=file,
    help="path to text file that needs to be translated"
)

exclusive.add_argument(
    "-t", "--text",
    metavar="TEXT", nargs="+",
    help="text that needs to be translated"
)

# Argument group for optional arguments
optional = parser.add_argument_group("optional arguments")

optional.add_argument(
    "-p", "--prefix-chance",
    metavar="CHANCE", type=chance, default=1.0,
    help="chance of getting a prefix, must be within 0 and 1"
)

optional.add_argument(
    "-s", "--suffix-chance",
    metavar="CHANCE", type=chance, default=1.0,
    help="chance of getting a suffix, must be within 0 and 1"
)

# argument group for miscellaneous arguments
misc = parser.add_argument_group("miscellaneous arguments")

misc.add_argument(
    "--help", action="help",
    help="show this help message and exit"
)

misc.add_argument(
    "--version", action="version",
    version=__version__
)


def main(args=None):
    """Parse arguments and print results."""
    args = parser.parse_args()

    # Show usage if there are no inputs
    if args.text is None and args.input_file is None:
        parser.print_usage()
        sys.exit(1)
    # When -t/--text is used
    elif args.text is not None:
        # nargs '+' results in a list
        args.text = " ".join(args.text)
    # When -f/--file is used
    elif args.input_file is not None:
        try:
            with open(args.input_file, encoding="utf-8") as file:
                args.text = file.read()
        except UnicodeDecodeError:
            print("Could not decode file as UTF-8.")
            print(sys.exc_info()[1])
            sys.exit(1)

    # Output the results
    print(owoify(
        args.text,
        prefix_chance=args.prefix_chance,
        suffix_chance=args.suffix_chance
    ))
