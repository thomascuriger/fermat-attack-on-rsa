import math
import random

# utility functions
# (x^y) % p
def moduloMult(x, y, p):
    res = 1;
    x = x % p;
    while (y > 0):
        if (y & 1):
            res = (res * x) % p;
        y = y >> 1;
        x = (x * x) % p;
    return res;

def extendedGcd(x, y):
    if (x == 0):
        return 0, 1
    u, v = extendedGcd(y % x, x)
    a = v - (y // x) * u
    b = u
    return a, b

def generatePrime(n, k):
    while (isMillerRabinPrime(n, k) == False):
        n+=1;
    return n;

# pre: n number, k no of tries
def isMillerRabinPrime(n, k):
    d = n - 1;
    while (d%2 == 0):
        d //= 2;
    for i in range(k):
        if (millerRabinTest(d, n) == False):
            return False
    return True

def millerRabinTest(d, n):
    a = 2 + random.randint(1, n-4)
    x = moduloMult(a, d, n);
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
    return False;


def calculateRSA():
    y = random.randint(1, MAX_PRIME_LENGTH);
    # y big number
    p = generatePrime(y, 10000);
    print("prime p: ", p);
    # q next higher than p
    space = random.randint(p, MAX_PRIME_LENGTH)
    q = generatePrime(space, 10000);
    print("prime q: ", q);
    # get exponent e
    randE = random.randint(math.pow(2, 16), math.pow(2, 64));
    e = generatePrime(randE, 100000);
    print("exponent: ", e);
    N = p * q;
    print("module: ", N)
    phi = (p - 1) * (q-1);
    d, k = extendedGcd(e, phi);
    if (d < 0):
        d += phi;
    print("private key: ", d);
    print("public key e, N:", e, N);
    print("rsa calculated")
    executeFermatAttack(e, N, d)
    return True;

def executeFermatAttack(e, N, d):
    # given: e, N
    # wanted: p, q
    startVal = math.isqrt(N);
    a, b, tries = attack(startVal, N)
    p = a - b;
    q = a + b;
    print(p, q, tries)
    return True

def attack(estimate, N):
    for tries in range(MAX_NO_OF_TRIES):
        b = pow(estimate + tries, 2) - N
        if b >= 0 and pow(math.isqrt(b),2) == b:
            return estimate + tries, math.isqrt(b), tries + 1
    return 0, 0, MAX_NO_OF_TRIES

def getStatistic(results):
    hacked = 0
    clear = 0
    for result in results:
        if (result):
            hacked += 1
        else:
            clear += 1
    print("calc quote")

def main():
    calculateRSA()

MAX_NO_OF_TRIES = 10000000
MAX_PRIME_LENGTH = 42949672961
main()