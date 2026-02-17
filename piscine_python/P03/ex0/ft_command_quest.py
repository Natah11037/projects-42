#!/usr/bin/env python3

import sys


def command_quest():
    program_name = sys.argv[0]
    arg = sys.argv[1:]
    i = 1
    if not arg:
        print("No arguments provided ! (need at least 1)")
        print(f"Program name: {program_name}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {len(arg)}")
        for each_arg in arg:
            print(f"Argument {i}: {each_arg}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
