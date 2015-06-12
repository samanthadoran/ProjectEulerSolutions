proc problem1(n: int): int =
    for i in 0..n - 1:
        if i mod 3 == 0 or i mod 5 == 0:
            result = result + i
echo(problem1(1_000))