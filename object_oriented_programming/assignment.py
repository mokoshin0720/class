def factorial(num: int) -> int:
    tmp = 1
    for i in range(1, num+1):
        tmp *= i
    return tmp

if __name__ == "__main__":
    ans = factorial(39)
    print(ans)