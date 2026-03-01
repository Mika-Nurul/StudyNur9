import turtle as t
t.speed(0)
co = "FLFRRFLF"
r = 2
a = 60
b = 60
q = int(input())
for u in range(3):
    for c in co:
        if c == "F":
            t.forward(r)
        elif c == "R":
            t.right(a)
        elif c == "L":
            t.left(a)
    for i in range(q):
        for j in com:
            if j == "F" :
                co = co.replace("F", "FLFRRFLF")
    t.right(120)
t.done()
