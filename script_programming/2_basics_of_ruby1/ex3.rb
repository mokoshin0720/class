def is_prime(n)
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

begin
    num = gets.to_i
    if num < 2
        raise "2以上の整数を入力してください"
    end
rescue => e
    puts e.message
    retry
end

if is_prime(num)
    print("Yes")
else
    print("No")
end