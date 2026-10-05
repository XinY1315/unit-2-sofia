""" def spaces(N, y, t):
    occupied = 0
    for i in range(N):
        #len can be used in place of n in case n is not given
        y[i] and t[i]
        if y[i] == "C" and t[i] == "C":
            occupied+=1
    return occupied
print(spaces(5, "CC..C", ".CC..")) """

""" def letters(N, English, French):
    for i in range(N):
        if "T" + "t" > "s" + "S":
            print(English)
        elif "S" + "s" > "T" + "t":
            print(French)
        else:
            print(English) """

def wizard(owner, N, duels):
    #who owns the wand
    last_owner = owner
    #number of duels
    changes = 0
    #check one single battle
    print(duels[0])
    #check first character
    print(duels[0][0])
    #check if wand changed hands
    if 
wizard("A", 3, ["BA", "CB", "DA"])