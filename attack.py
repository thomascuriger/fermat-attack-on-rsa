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


def calculateRSA(l):
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
    dTemp = extendedGcd(e, phi);
    d = dTemp[0]
    if (d < 0):
        d += phi;
    print("private key: ", d);
    print("public key e, N:", e, N);
    print("rsa calculated")
    return True;

def executeFermatAttack(numberOfAttacks, max):
    # given: e, N
    # wanted: d
    print("execute it")
    return True

def getRsaD(p,q):
    return max(p,q)

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
    MAX_NO_OF_TRIES = 100000
    testcases = getTestCases()
    results = []
    i = 0
    for case in testcases:
        results[i] = executeFermatAttack(case, MAX_NO_OF_TRIES)
        i += 1
    getStatistic(results)

#main()
extendedGcd(10,25)
MAX_PRIME_LENGTH = 4294967296
calculateRSA(1)
# isMillerRabinPrime(7761, 10)
# works