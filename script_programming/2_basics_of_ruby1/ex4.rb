ans = []
while true
    print("数値?")
    num = gets.to_i

    if num < 0
        puts("0より大きな数を入力してください")
        next
    end

    if num == 0
        ans.size.times do |num|
            puts(ans.pop)
        end
        break
    end
    
    ans.push(num)
end