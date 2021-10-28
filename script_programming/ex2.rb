def is_prime(n)
    # 1の判定
    if n == 1
        return false
    end
    # 2の判定
    if n == 2
        return true
    end

    # 3以上の判定
    prime_numbers = [2]
    flag = true

    (3..n).each do |i|
        flag = true
        prime_numbers.each do |number|
            if i % number == 0
                flag = false
                break
            end
        end

        if flag
            prime_numbers.push(i)
        end
    end

    return flag
end

if is_prime(gets.to_i)
    print("Yes")
else
    print("No")
end