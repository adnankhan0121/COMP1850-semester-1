"""
Look-up tables for transforming greyscale Image objects.

Usage:
    python lookup_tables.py <input.pgm> <output.pgm> [invert|sqrt|brighten|darken]
"""

import math
import sys

from image import Image


class LookupTable:
    """
    A generic LUT. Pre-computes function(x) for every possible pixel
    value 0..max_value and stores the results in a list.
    Subclasses change the mapping by overriding function().
    """

    def __init__(self, max_value=255):
        self.max_value = max_value
        self.table = [self.function(x) for x in range(max_value + 1)]

    def function(self, x):
        """Identity mapping: leaves pixel values unchanged."""
        return x

    def display(self):
        """Prints the mapping of pixel values performed by this LUT."""
        for x, y in enumerate(self.table):
            print(f"{x:3d} -> {y:3d}")

    def apply_in_place(self, image):
        """Modifies the given image by passing every pixel through the LUT."""
        if image.max_value > self.max_value:
            raise ValueError("image has pixel values beyond this LUT's range")
        for i in range(image.width * image.height):
            image[i] = self.table[image[i]]

    def apply(self, image):
        """Returns a new image: a copy of the given image passed through the LUT."""
        result = image.copy()
        self.apply_in_place(result)
        return result


class InvertLUT(LookupTable):
    """f(x) = max - x: white becomes black and vice versa."""

    def function(self, x):
        return self.max_value - x


class SqrtLUT(LookupTable):
    """Square root scaled so 0..max still maps to 0..max."""

    def function(self, x):
        return round(math.sqrt(x * self.max_value))


class BrightnessLUT(LookupTable):
    """f(x) = x + offset, clamped to the range 0..max."""

    def __init__(self, offset, max_value=255):
        # Must be set BEFORE super().__init__(), because that calls function()
        self.offset = offset
        super().__init__(max_value)

    def function(self, x):
        return min(max(x + self.offset, 0), self.max_value)


LUTS = {
    "invert": lambda: InvertLUT(),
    "sqrt": lambda: SqrtLUT(),
    "brighten": lambda: BrightnessLUT(50),
    "darken": lambda: BrightnessLUT(-50),
}


def main():
    if len(sys.argv) not in (3, 4):
        print("Usage: python lookup_tables.py <input.pgm> <output.pgm> [invert|sqrt|brighten|darken]")
        sys.exit(1)

    infile, outfile = sys.argv[1], sys.argv[2]
    choice = sys.argv[3] if len(sys.argv) == 4 else "invert"
    if choice not in LUTS:
        print(f"Unknown LUT '{choice}'. Choose from: {', '.join(LUTS)}")
        sys.exit(1)

    lut = LUTS[choice]()
    lut.display()

    img = Image.read(infile)
    result = lut.apply(img)
    result.write_pgm(outfile)
    print(f"Applied {choice} LUT to {infile}, wrote {outfile}")


if __name__ == "__main__":
    main()