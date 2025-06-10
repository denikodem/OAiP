def prost_sloz(n, d=2):
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return prost_sloz(n, d + 1)
