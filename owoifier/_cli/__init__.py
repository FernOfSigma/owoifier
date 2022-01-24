# Copyright (C) 2021 FernOfSigma.

# This file is part of owoifier.

# owoifier is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# owoifier is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# owoifer. If not, see <https://www.gnu.org/licenses/>.

"""Parses the arguments and outputs result."""

import sys

from .interface import argparser
from ..owoifier import owoify


def handle_text(args):
    """Handle arguments for text input."""
    print(owoify(
        args.text,
        prefix=args.add_prefix,
        suffix=args.add_suffix
    ))

def handle_file(args):
    """Handle arguments for file input."""
    try:
        with open(args.input_file, encoding="utf-8") as file:
            args.text = file.read()
            handle_text(args)
    except UnicodeDecodeError:
        print("Could not decode file as UTF-8.")
        sys.exit(1)

def main():
    """This was funny in my head."""
    args = argparser.parse_args()
    if args.text is not None:
        args.text = " ".join(args.text)
        handle_text(args)
    elif args.input_file is not None:
        handle_file(args)