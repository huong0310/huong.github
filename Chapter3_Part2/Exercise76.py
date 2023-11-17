n = int(input("Enter an integer (2 or greater): "))
if n < 2:
    print("Error: Hãy nhập một số nguyên lớn hơn hoặc bằng 2")
else:
    print("the prime factors of",n,"are")
    factor = 2
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n = n // factor
        else:
            factor = factor + 1