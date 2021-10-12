# 数値を取得
num = gets.to_i

# 三角形を作る処理
(1..num).each do |n|
    blank = num-n
    star = (2*n)-1

    (1..blank).each do |b|
        print(" ")
    end
    (1..star).each do |s|
        print("*")
    end
    (1..blank).each do |b|
        print(" ")
    end
    puts
end