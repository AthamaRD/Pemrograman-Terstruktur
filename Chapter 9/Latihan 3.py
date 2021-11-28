def star(n):
    star = 2*n-1
    if 9%2 == 0:
        for i in reversed(range(n//2)):
           print(("*"*(i*2+1)).center(star))
        for i in range(n//2):
           print(("*"*(i*2+1)).center(star))
    else:
        for i in range(n//2):
           print(("*"*(i*2+1)).center(star))
        for i in reversed(range(n//2+1)):
           print(("*"*(i*2+1)).center(star))

star(9)