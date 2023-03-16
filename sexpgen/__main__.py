from .sexpgen import from_file
from sys import argv

if len(argv) > 1 and (path := argv[-1]):
    from_file(path)

