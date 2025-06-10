from gear import gears
def main():
    i = int(input("Введите количество строк: "))
    data = [list(map(int, input(">>> ").split())) for _ in range(i)]
    n = int(input("передаточное n: "))
    m = int(input("передаточное m: "))
    result = gears(data, n, m)
    print(result)

if __name__ == "__main__":
    main()
