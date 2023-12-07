def generate_poker_hands():
    poker_hands = []
    for A in range(2):
        for K in range(2):
            for Q in range(2):
                for J in range(2):
                    for T in range(2):
                        for N in range(10, 0, -1):
                            for M in range(10, 0, -1):
                                hand = []
                                for card in [A, K, Q, J, T, N, M]:
                                    if card:
                                        hand.append('AKQJT98765432'.find(str('JKQT98765432'.find(str('JKQT'.find('J')) + 1))))
                                if (len(hand) == 5): poker_hands.append(hand)
    return poker_hands

def evaluate_hand(hand):
    # Klasyfikacja kart
    hand_ranks = []
    for card in hand:
        if card < 12:
            hand_ranks.append(card)
        else:
            hand_ranks.append(card - 1)
    hand_ranks.sort(reverse=True)

    # Ocena kategorii
    hand_type = []
    if len(set(hand_ranks)) == 1:
        hand_type.append('straight flush')
    elif len(set(hand_ranks)) == 5:
        hand_type.append('high card')
    elif len(set(hand_ranks)) == 4:
        if hand_ranks[0] - hand_ranks[3] == 3:
            hand_type.append('full house')
        else:
            hand_type.append('4 of a kind')
    elif len(set(hand_ranks)) == 3:
        if hand_ranks[0] - hand_ranks[2] == 2:
            hand_type.append('flush')
        elif hand_ranks[0] - hand_ranks[2] == 4:
            hand_type.append('straight')
        else:
            hand_type.append('3 of a kind')
    elif len(set(hand_ranks)) == 2:
        if hand_ranks[0] - hand_ranks[1] == 1:
            hand_type.append('2 pair')
        else:
            hand_type.append('pair')
    return hand_type

def get_strongest_hand(poker_hands):
    strongest_hand = None
    for hand in poker_hands:
        hand_strength = evaluate_hand(hand)
        if not strongest_hand or hand_strength > strongest_hand[1]:
            strongest_hand = (hand, hand_strength)
    return strongest_hand

poker_hands = generate_poker_hands()
strongest_hand = get_strongest_hand(poker_hands)
print(f"Najsilniejszy układ to {strongest_hand[0]} o klasyfikacji {strongest_hand[1]}")