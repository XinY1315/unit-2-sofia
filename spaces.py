def spaces(N, y, t):
    occupied = 0
    for i in range(N):
        #len can be used in place of n in case n is not given
        y[i] and t[i]
        if y[i] == "C" and t[i] == "C":
            occupied+=1
    return occupied
print(spaces(5, "CC..C", ".CC.."))