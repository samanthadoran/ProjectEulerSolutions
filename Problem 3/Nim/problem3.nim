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

#Return the largest prime factor of n
proc problem3(n: int64): int =
    var largestPrimeFactor: int = 3
    for i in countup(3, int sqrt(float n) + 1, 2):
        if n mod i == 0 and isPrime(i):
            if i > largestPrimeFactor:
                largestPrimeFactor = i
    return largestPrimeFactor


echo(problem3(600851475143))
