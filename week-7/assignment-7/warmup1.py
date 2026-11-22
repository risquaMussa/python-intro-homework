with open("../data/notes.txt", "r") as file:
    lines = file.readlines()

    counter = 1
    for line in lines:
        print(f"Line {counter}: {line.strip()}")
        counter += 1