import turtle as t
t.shape("turtle")
t.color("green")
t.hideturtle()
'''brc - branches count brdist - branches distance brst - branches step '''
def el(brc,brdist,brst):
    t.speed(10)
    angle = 45
    st = 50
    fd = 15
    t.teleport(0,st + brdist*(brc - 1))
    for i in range(brc):
        t.setheading(270)
        t.left(angle)
        t.forward(fd)
        t.right(180)
        t.forward(fd)
        t.left(90)
        t.forward(fd)
        t.right(180)
        t.forward(fd)
        t.right(180 - angle)
        t.forward(brdist)
        fd += brst
    t.forward(st)
elka(6,30,15)
t.done()
