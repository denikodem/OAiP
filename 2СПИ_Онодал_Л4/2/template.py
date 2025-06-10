def template(a, b, c):

    # Периметр #
    P = a + b + c

    # Площадь через герона#
    pp = P / 2
    S = (pp * (pp - a) * (pp - b) * (pp - c)) ** 0.5

    status_rav = ' '
    status_ravbed = ' '

    # проверка на равнобедренность #
    if (a == c and a != b and c != b) or (c == b and c != a and b != a) or (a == b and a != c and b != c):
        status_ravbed = 'да'
    else:
        status_ravbed = 'нет'

    # проверка на равностороность #
    if a == b and b == c and c == a:
        status_rav = 'да'
    else:
        status_rav = 'нет'


    print(f'''
Периметр: {P}
Площадь: {S}
Равнобедренный: {status_ravbed}
Равносторонний: {status_rav}
''')

pass