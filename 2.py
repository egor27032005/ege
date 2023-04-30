## ((¬z⋁¬x)⋀z)⋁w⋁¬y
print("x y z F")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            F= (not x or not z)<=(x==y)
            if F==0:
                print(x, y, z, F)