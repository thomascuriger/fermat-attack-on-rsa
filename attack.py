import math

def generatePrime():
    print("prime generated")

def calculateRSA():
    print("rsa calculated")
    print("keys")

def executeFermatAttack(numberOfAttacks, max):
    # given: e, N
    # wanted: d
    print("execute it")
    return True

def getTestCases():
    primeOne = generatePrime()
    primeTwo = generatePrime()
    print("generate testcases")

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