import math
discard """Returns the difference between the square of the sum of the first n 
        natural numbers and the sum for the first n squares"""
proc problem6(n: int): int = 
    var squareOfSum: int = int pow(float n * (n + 1) div 2, float 2)
    var sumOfSquares = 0
    for i in 0..n:
        sumOfSquares += i * i
    return squareOfSum - sumOfSquares

echo(problem6(100))
