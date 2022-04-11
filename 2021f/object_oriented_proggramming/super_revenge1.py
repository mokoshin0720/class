month_day = int(input())
month_day += 1
exception_dic = {
    132: 201,
    229: 301,
    332: 401,
    431: 501,
    532: 601,
    631: 701,
    732: 801,
    832: 901,
    931: 1001,
    1032: 1101,
    1131: 1201,
    1232: 101,
}

for k, v in exception_dic.items():
    if month_day == k:
        month_day = exception_dic[k]

print(month_day)
print(f"{month_day//100}月{month_day%100}日")