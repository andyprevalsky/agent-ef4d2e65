#!/usr/bin/env python3
"""Print the Collatz sequence from a starting number down to 1.

Usage: python3 collatz.py [start]   (start defaults to 27)
"""
import sys


def collatz_sequence(n):
    """Return the Collatz sequence from n to 1, inclusive of both ends."""
    if n < 1:
        raise ValueError("start must be a positive integer")
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main(argv):
    start = int(argv[1]) if len(argv) > 1 else 27
    sequence = collatz_sequence(start)
    for number in sequence:
        print(number)
    # Steps are transitions between numbers, so the initial number is not counted.
    print(f"Total steps: {len(sequence) - 1}")


if __name__ == "__main__":
    main(sys.argv)
