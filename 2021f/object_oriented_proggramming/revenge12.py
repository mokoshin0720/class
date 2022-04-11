def question4():
    print("自然数を入力してください。")
    x=int(input())
    num=0
    for i in range(1,x+1):
        d=x%i
        if d==0:
            num+=1
    print("%dの約数の個数は%d個です。" % (x, num))
    
def question5(start, end):
    cnt = 0
    for c in range(start,end):
        for b in range(start,c):
            for a in range(start,b):
                if a*a+b*b==c*c:
                    print(a,b,c)
                    cnt += 1
    print(cnt)

def question6(start, end):
    cnt = 0
    for c in range(start,end):
        for b in range(start,c):
            for a in range(start,b):
                if a*a+b*b==c*c:
                    if 50 <= a*b//2 <= 150:
                        print(a*b//2)
                        cnt += 1
    print(cnt)
question6(1, 31)