def horse2(cell):
    x = ord(cell[0]) - ord('a') + 1
    y = int(cell[1:])
    moves = [
        (x + 2, y + 1), (x + 2, y - 1),
        (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2),
        (x - 1, y + 2), (x - 1, y - 2)
    ]
    result = []
    for mx, my in moves:
        if 1 <= mx <= 8 and 1 <= my <= 8:
            col = chr(ord('a') + mx - 1)
            result.append(f"{col}{my}\n")
    return sorted(result)
