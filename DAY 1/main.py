pos = 50
zero_count = 0

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        direction = line[0].upper()
        value = int(line[1:])

        if direction == "L":
            ...

        elif direction == "R":
            ...

        else:
            raise ValueError(f"Invalid direction: {direction}")
            ...
print("Times dial hit 0:", zero_count)
