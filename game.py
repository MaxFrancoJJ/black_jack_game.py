import build

playing = True

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11')


    # Create & shuffle dethe deck, deal two cards to each player
    deck = build.Deck()
    deck.shuffle()

    player_hand = build.Hand() #instantiate player hand
    player_hand.add_card(deck.deal()) #deal first card
    player_hand.add_card(deck.deal()) #deal second card

    dealer_hand = build.Hand() #instantiate dealers hand
    dealer_hand.add_card(deck.deal())  #deal first card
    dealer_hand.add_card(deck.deal()) #deal second card (hidden)

    # Set up the Player's chips
    player_chips = build.Chips()


    # Prompt the Player for their bet
    build.take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    build.show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        build.hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        build.show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            build.player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                build.hit(deck, dealer_hand)

        # Show all cards
        build.show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if dealer_hand.value > 21:
            build.dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            build.dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            build.player_wins(player_hand, dealer_hand, player_chips)
        else:
            build.push(player_hand, dealer_hand)


    # Inform Player of their chips total
    print(f"\nPlayer total chips: {player_chips.total}")
    # Ask to play again
    new_game = input("Would like to play another hand? yes or no")

    if new_game[0].lower():
        playing = True
        continue
    else:
        print("Thank you for playing")

    break
