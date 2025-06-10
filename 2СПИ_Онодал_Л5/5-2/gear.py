def gears(data, n, m):
    all_gears = [x for group in data for x in group]
    max_a, max_b = None, None
    for i in range(len(all_gears)):
        for j in range(len(all_gears)):
            if i != j and all_gears[j] != 0 and all_gears[i] / all_gears[j] == n / m:
                if max_a is None or all_gears[i] > max_a:
                    max_a, max_b = all_gears[i], all_gears[j]
    return (max_a, max_b)