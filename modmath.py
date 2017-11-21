def modularPow(base, exp, mod):
    result = 1
    while (exp > 0):
        if (exp % 2 == 1):
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result;

def modularExp(base, exp, mult, mod):
    result = 1
    baseMult = base*mult
    while (exp > 0):
        if (exp % 2 == 1):
            result = (result * baseMult) % mod
        exp = exp >> 1
        baseMult = (baseMult * base) % mod
    return result

def modulo(n, p):
    r = n%p;
    if( ((p > 0) and (r < 0)) or ((p < 0) and (r > 0)) ):
        r += p
    return r

def modInverse(n, mod):
    n = modulo(n, mod)
    for x in range(mod):
        if(modulo(n*x, mod) == 1):
            return x
    return 0
