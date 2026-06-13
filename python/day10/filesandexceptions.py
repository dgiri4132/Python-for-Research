# Learning files and exceptions
with open('python/day10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

"""File Paths
    When you pass a simple filename, python looks in the directory where the file that's currently
    being executed is stored. Normally python only looks at the directory and stops
    if you want to do that, you need a file path, which tells a specific place to look at
"""


