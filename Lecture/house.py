name = input("What's your name?")

match name:
    case "Harry" | "Tim" | "Helen":
        print("Gryffindor")
    case "Don":
        print("Slytherin")
    case _:
        print("Who?")