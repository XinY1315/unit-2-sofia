""" day_of_week = input("What day of the week is it?")
if day_of_week == "Monday":
    print("noooooo")
else: 
    print("go to sleep") """

""" temp = 75
if temp > 70:
    print('warm')
elif temp == 70:
    print('just right')
else:
    print('coldcoldcold') """

#use max/min for smaller and bigger number
#also can use "and" to check both at the same time
#check for "i"

#must write full expression or you fail

""" user = input("Write a sentence.")
def sentence(N, x):
    words = 0
    for i in range(N):
        x[i]
        if x[i] == " ":
            words += 1
    return words  """

"""def odd_or_even(number):
    if number%2 == 1:
        print("odd")
    else:
        print("even")

number = input("type a number") """

#TEST DAY INDEX CARD can have a loop example, example function, notes
def total(service, bill):
    if service == "bad":
        tip_percentage = 0
    elif service == "okay":
        tip_percentage = 0.15
    elif service == "good":
        tip_percentage = 0.2
    else:
        tip_percentage = 0.25
    tip = int(bill*tip_percentage)
    total_amount = (bill+tip)
    print(tip)
    print(total_amount)
bill = float(input("How much is the bill?"))
service = input("How was the service?")
total(bill, service)