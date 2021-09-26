def sieve_of_eratosthenes(num: int) -> [int]:
    nums = [i for i in range(num+1)]
    
    root = int(pow(num, 0.5))
    for i in range(2, root+1):
        if nums[i] != 0:
            for j in range(i, num+1):
                if i*j >= num+1:
                    break
                nums[i*j] = 0
    
    return sorted(list(set(nums)))[2:]

if __name__ == "__main__":
    ans = sieve_of_eratosthenes(100)
    print(ans)