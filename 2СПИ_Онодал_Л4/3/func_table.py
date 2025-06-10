def func_table(f, x_max, y_max):
    table = []
    for y in range(y_max + 1):
        row = []
        for x in range(x_max + 1):
            value = eval(f)
            row.append(str(value))
        table.append(row)
    for x in range(x_max + 1):
        col = [table[y][x] for y in range(y_max + 1)]
        print('\t'.join(col))
pass