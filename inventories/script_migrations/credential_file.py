#!/usr/bin/env python3

from __future__ import print_function
import os, sys

# Reads from a file that is laid down by a custom AWX credential

print(open(os.environ["AWX_CUSTOM_INI"]).read(), file=sys.stderr)
print("{}")
