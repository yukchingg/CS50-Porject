import argparse

parser = argparse.ArgumentParser(description="Meow Like a cat")
parser.add_argument("-n", default=1, help="number of time to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")