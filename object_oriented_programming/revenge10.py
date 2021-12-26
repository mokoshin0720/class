import datetime

ym = int( input( "西暦年月を6桁で入力:" ) )
year, month = ym // 100, ym % 100

youbi = "日月火水木金土"
cal = datetime.date( year, month, 1)
print(f"{cal.year}年{cal.month}月")

print( "Sun Mon Tue Wed Thu Fri Sat" )
startday = cal.isoweekday()
limitday = 31
day = 1
for n in range( startday ): print( end="    " )
while day <= limitday:
    print( f"{day:3}", end=" " )
    if (startday + day) % 7 == 0: print( )
    day += 1
print()