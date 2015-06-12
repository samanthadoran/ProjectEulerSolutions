#Reverses a string
proc reverse(s: string): string =
    result = ""
    for i in countdown(s.len - 1, 0):
        result = result & $s[i]

#Finds the largest palindrome number that is formed by multiplying two 3 digit numbers together
proc problem4(): int =
    for j in 100..999:
        for k in 100..999:
            if $(j * k) == reverse($(j * k)):
                if j * k > result:
                    result = j * k

echo(problem4())