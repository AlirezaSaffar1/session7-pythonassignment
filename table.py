def jadval_zarb():
    row = int(input("enter row: "))
    col = int(input("enter col: "))
    for i in range(1, row+1):
        for j in range(1, col+1):
            if i == 0 and j == 0:
                print("X", end="\t")
            elif i == 0 :
                print(j-1, end="\t")
            elif j == 0 :
                print(i-1, end="\t")
            else:
                print((i-1)*(j-1), end="\t")
        print()

print("Hi! I can help you multipy numbers. Enter your rows and columns: ")
jadval_zarb()