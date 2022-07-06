import math

def generatePrime():
    print("prime generated")

def isMillerRabinPrime():
    print("check prime")


def calculateRSA():
    p = generatePrime()
    q = generatePrime()
    higher = max(p,q)
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

main()