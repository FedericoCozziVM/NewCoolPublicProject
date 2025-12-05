import math
import sys


def compute_square_root(number: float) -> float:
    """
    Compute the square root of a given number.

    Args:
        number: The number to compute the square root of.

    Returns:
        The square root of the number.

    Raises:
        ValueError: If the number is negative.
    """
    if number < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(number)

# This change should be reflected in mirrored repo
# Also this comment
# And this
# And this also
# Maybe the last?
# pls


def main():
    """Main function to run the square root calculator."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <number>")
        print("Example: python main.py 16")
        sys.exit(1)

    try:
        number = float(sys.argv[1])
        result = compute_square_root(number)
        print(f"The square root of {number} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
