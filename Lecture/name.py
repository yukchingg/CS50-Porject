import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("Hello, my name is ", sys.argv[1])

if len(sys.argv) <2:
    sys.exit("Too few arguments")

for argv in sys.argv[1:]:
    print(argv)