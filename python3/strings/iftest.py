#!/usr/bin/env python3.2

digit = "0python"

def main(x):
    if x[0] in "0987654321":
        return False
    else:
        return True

print(main(digit))

