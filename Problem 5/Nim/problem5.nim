proc problem5(): int =
    var i: int = 19
    while true:
        i += 1
        for k in 1..20:
            if i mod k == 0:
                if k == 20:
                    return i
                continue
            if i mod k != 0:
                break
echo(problem4())