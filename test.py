
def blabla():
    y = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

    if y[0].lower() == 'h':
        hit(deck,hand)
    elif y[0].lower == 's':
        print(y[0])
        print('Player stands. Dealer playing')
        playing = False
    else:
        print("Sorry, i can't understand, try again")

blabla()
