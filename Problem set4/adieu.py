import inflect

p = inflect.engine()

try:
    names = []
    while True:
        names.append(input("Name: "))
except EOFError:
    pass

print("Adieu, adieu, to", p.join(names) )