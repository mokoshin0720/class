days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

n = int(input("4桁の値を入力: "))
day, month = n%100, n//100
answer = sum(days[:month-1])
print(answer+day, "日目")