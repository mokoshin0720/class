def question2(y):
    return y%10 + y%100//10 == 10

def question3(x, y):
    return 360%x == 0 or 360%y == 0

def question4(x, y):
    return y**x if x%2 == 0 else y**3 if x%3 == 0 else y**4

print(question4(5, 10))