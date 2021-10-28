def arraycalc(x, y, func)
    ans = []
    x.length.times do |i|
        tmp = func.call x[i],y[i]
        ans.push(tmp)
    end
    return ans
end

# ans = arraycalc([1, 2, 3], [4, 5, 6], lambda{|x,y| x*y})
# print(ans)