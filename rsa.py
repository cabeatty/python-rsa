# Transformation for the blocks will be done in the form E(P) = C ≡ P^e (mod n)
# where n is a pseudoprime with two prime factors, p & q, and we have (e, φ(n)) = 1
# Again, for ease of use, for the time being I am going to have these variables
# provided as immutable in this class.  e, n, p & q defined as following
# e=13
# n=2537
# p=43
# q=59
# Note that (13, φ(2537)) = 1
# And thus C ≡ P^13 (mod 2537)

import block
import modmath

exp = 13
mod = 2537
p = 43
q = 59

def encrypt(input):
    input, output = block.st2bv(input), []
    print(input)
    for i in range(len(input)):
        temp = modmath.modularPow(input[i], exp, mod)
        output.append(temp)
    return output

def decrypt(input):
    dmod, output = (p-1)*(q-1), []
    expInv = modmath.modInverse(exp, dmod)
    for i in range(len(input)):
        temp = modmath.modularPow(input[i], expInv, mod)
        output.append(temp)
    return output
