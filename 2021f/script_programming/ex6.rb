max_length = 0
ans = ""
IO.foreach("CROSSWD.txt") do |line|
    if line.length > max_length
        max_length = line.length
        ans = line
    end
end
puts ans