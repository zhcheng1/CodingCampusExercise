
l = []

with open("map.txt", "r") as file:
    for line in file:
        l.append([])
        for item in line:
            if item != "\n":
                l[-1].append(item)


def floodfill(x, y, old_symbol, new_symbol):

    if l[x][y] != old_symbol:
        return

    if l[x][y] not in l:


    l[x][y] = new_symbol

    floodfill(x+1, y, old_symbol, new_symbol)
    floodfill(x-1, y, old_symbol, new_symbol)
    floodfill(x, y+1, old_symbol, new_symbol)
    floodfill(x, y-1, old_symbol, new_symbol)


floodfill(0, 0, ".", "s")

for line in l:
    print line







