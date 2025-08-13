#!/usr/bin/env python3

import sys


def copy_program_to_readme(programs_to_write):
    for program in programs_to_write:
        with open("README.md", "a") as file:
            file.write(f"{program}\n")
    print("New Program(s) installed!")

copy_program_to_readme(sys.argv[1:])

