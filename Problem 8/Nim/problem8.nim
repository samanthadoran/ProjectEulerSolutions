import strutils
#Parse a number from a file into a string
proc getNumFromFile(filename: string): string = 
    var f: File
    if open(f, filename):
        var num = ""
        for line in f.lines:
            num = num & line
        f.close
        return num
    else:
        echo("Failed to open file...")
        return ""


#Find the largest product of 13 adjacent digits in a number
proc problem8(): int64 =
    var num = getNumFromFile("numbers.txt")
    var maxProduct = 1
    var currProduct = 1
    for i in countup(0, num.len - 13):
        for j in countup(0, 13 - 1):
            currProduct *= parseInt($num[i + j])
        if currProduct > maxProduct:
            maxProduct = currProduct
        currProduct = 1
    return maxProduct

echo(problem8())