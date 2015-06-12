import math

#Find the pythagorean triplet for which a + b + c = 1000
proc problem9(): int =
    for a in 1..1000:
        for b in 1..1000:
            var c = sqrt(float a * a + b * b)
            if c mod 1 == 0:
                if a + b + (int c) == 1000:
                    return (a * b * int c)

echo(problem9())