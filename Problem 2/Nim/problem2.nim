#Sum even fibonacci numbers below n
proc problem2(n: int): int =
    var
        x = 1
        y = 1
        swap = 0
    while y < n:
        if y mod 2 == 0:
            result += y
        swap = x
        x = y
        y = swap + x

echo(problem2(4_000_000))