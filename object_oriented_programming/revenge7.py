def question2():
    for n in range( 1, 10 ): print( 10-n if n % 2 == 0 else n**3, end=" " )

def question3():
    for n in range( 1, 10 ): print( (3-n%3) ** 2, end=" " )

def question4():
    for n in range( 726, 794, 17 ): print( (n % 123) ** (n%12), end=" " )

def question5():
    summ = 0
    for i in range(1, 361):
        if 360%i == 0 and 12 <= i <= 90: summ += i
    print(summ)

question5()