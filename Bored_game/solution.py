mod = 123454321
def answer(rolls, cells):
    start = 1
    turns = 1
    prev_paths = [0]*cells
    cur_paths = [0]*cells
    new = 0
    #Base cases
    if cells-rolls > 1:
        return 0
    elif cells == 2:
        return rolls
    elif cells ==  rolls:
        return cells
    else:
        while cells < rolls:
            if turns < (cells - 1):
                turns+=1
            j = 0
            while (j<cells) and (j<turns+1):
                if j==0:
                    cur_paths[j] = prev_paths[j] + prev_paths[j+1]
                    j+=1
                elif j == turns:
                    if j == (cells - 1):
                        new += prev_paths[j-1]
                        j+=1
                    else:
                        cur_paths[j] = prev_paths[j-1]
                        j+=1
            prev_paths = cur_paths
        return new % mod