def question3(x, y):
    z = [1,36, 2,18, 3,12, 4,9, 6]
    print(x%36 == 0 and y in z)

def question4():
    n = int(input("4桁の値を入力： "))
    day, month = n%100, n//100
    print(f"{month}月{day}日")

def question5():
    n = int(input("数字を入力： "))
    if n > 12:
        print(f"{n}は範囲外です")

question5()