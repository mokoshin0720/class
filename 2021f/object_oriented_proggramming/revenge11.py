from turtle import *
tracer( False )
size, step = 250, 2
for n in range( 5 ):
    for m in range( 0, 270, step ):
        forward( step )
        right( step )
    forward( size )
done( )

# def drawRectangle(x, y, width, height):
    