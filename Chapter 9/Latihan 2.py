def star(n):
    for star in range(1, n):
        formasi = "*" * (1 +(star - 1) * 2)
        print(formasi.center(1 + 2 * n)) 

star(5)