def gcd_ext(a, b):
    if not b:
        return 1, 0, a
    y, x, g = gcd_ext(b, a % b)
    return x, y - (a // b) * x, g


def euklid(a, mod):
    t0 = gcd_ext(a, mod)[0]
    if t0 < 0:
        t0 += mod
    return t0


def quick_pow(base, pow_decimal, mod):
    pow_bin = []
    while pow_decimal:
        pow_bin.append(pow_decimal % 2)
        pow_decimal //= 2
    pow_bin.reverse()

    temp = base
    for i in pow_bin[1:]:
        temp = pow(temp, 2) % mod
        if i == 1:
            temp = (temp * base) % mod
    return temp


def find_roots(c, mod):
    a_pow2 = c % mod
    a1 = quick_pow(a_pow2, (mod + 1) / 4, mod)
    a2 = mod - a1
    return a1, a2


def calculate(p, q, c):
    m = p * q
    m1 = q
    m2 = p
    m1_rev = euklid(m1, p)
    m2_rev = euklid(m2, q)

    x12 = find_roots(c, p)
    x34 = find_roots(c, q)
    x = x12 + x34

    m11 = (x12[0] * m1 * m1_rev + x34[0] * m2 * m2_rev) % m
    m12 = (x12[0] * m1 * m1_rev + x34[1] * m2 * m2_rev) % m
    m13 = (x12[1] * m1 * m1_rev + x34[0] * m2 * m2_rev) % m
    m14 = (x12[1] * m1 * m1_rev + x34[1] * m2 * m2_rev) % m
    result = [m11, m12, m13, m14]
    result.sort()
    return result, m, m1, m2, m1_rev, m2_rev, x
