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
    y = random.randint(l, l + 18446744073709551616);
    # y big number
    p = generatePrime(y, 10000);
    print(p)
    # q next higher than p
    space = random.randint(p, 18446744073709551616)
    q = generatePrime(space, 10000);
    print(q)
    return True;
    higher = max(p,q); # sowieso q?
    n = p * q
    d = getRsaD(p,q)
    # d next great prime
    phi = (p-1)*(q-1)
    e = 0
    while (e < math.log2(n)):
        e = math.gcd(phi, d)
    print("rsa calculated")
    print("keys")

def gcd(phi, e):
    math.gcd(phi,e)

def executeFermatAttack(numberOfAttacks, max):
    # given: e, N
    # wanted: d
    print("execute it")
    return True

def getTestCases():
    p = generatePrime()
    q = generatePrime()
    d = getRsaD(p,q)
    print("generate testcases")

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
calculateRSA(5000000000000000)
# isMillerRabinPrime(7761, 10)
# works