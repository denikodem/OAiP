from horse import horse2


def main():
    cell = input("Введите клетку (например, e4): ").lower()
    moves = horse2(cell)
    print(''.join(moves))


if __name__ == "__main__":
    main()
