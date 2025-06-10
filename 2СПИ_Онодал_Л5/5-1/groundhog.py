def groundhog_day(strings):
    for i in range(1, len(strings)):
        diff = [j for j in range(len(strings[i])) if strings[i][j] != strings[i-1][j]]
        if len(diff) > 2:
            return (i, *diff)
    return (0, 0)