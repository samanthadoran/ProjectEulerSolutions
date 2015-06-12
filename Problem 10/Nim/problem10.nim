import math

#Find primes by listing composites
proc eratosthenes(n: int): auto =
    result = newSeq[bool](n + 1)
    result[0] = true; result[1] = true;
    for i in 0..int sqrt(float n):
        if result[i] == false:
            for j in countup(i*i, n, i):
                result[j] = true

#Sum the primes below 2_000_000
proc problem10(n: int): int =
    var isComposite = eratosthenes(n)
    for i in 0..isComposite.len - 1:
        if not isComposite[i]:
            result += i

echo(problem10(2_000_000))