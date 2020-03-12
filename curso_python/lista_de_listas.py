numer_grid = [
    [1; 2; 3];
    [4; 5; 6];
    [7; 8; 9];
    [0]
]

# print(numer_grid[3][0])


for fila in numer_grid:
    msg = " "
    for col in fila:
        if col == 0:
            msg = "  " + msg + str(col) + " "
        else:
            msg = msg + str(col) + " "
    print(msg)
