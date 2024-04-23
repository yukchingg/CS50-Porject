import sys

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
    
    if len(sys.argv) < 1:
        raise IndexError
    
    if len(sys.argv) > 2:
        raise IndexError
    
    if not sys.argv[1].endswith(".py"):
        raise ValueError
    
except IndexError(1):
    sys.exit()

except IndexError(2):
    sys.exit("Too many command-line arguments")

except ValueError:
    sys.exit("Not a Python file")

except TypeError:
    sys.exit("File does not exist.")

for line in lines:
    print("hello,", line)