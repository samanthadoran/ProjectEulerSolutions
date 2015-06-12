import math

#Determine if a given number is prime
proc isPrime(n: int64): bool =
    var factors: int = 0
    if n mod 2 == 0 and n != 2:
        return false
    for i in 1..int (sqrt(float n) + 1):
        if n mod i == 0:
            factors += 1
    return factors < 2

#Find the nth prime
proc problem7(n: int): int64 = 
    var index = 2
    var currentPrime = 3
    var currentNumber = 4
    while index < n:
        if isPrime(currentNumber):
            currentPrime = currentNumber
            index += 1
        currentNumber += 1
    return currentPrime

echo(problem7(10_001))