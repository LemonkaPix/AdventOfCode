from enum import Enum


print("--- Day 7: Camel Cards ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0
hands = []

symbols = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

class sequence(Enum):
    p = 7
    k = 6
    f = 5
    t = 4
    p2 = 3
    p1 = 2
    h = 1
    none = 0

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.rank = 0
        self.seq = 0

def IsGreaterThan(h1, h2):
    if h1.seq == h2.seq:
        for i in range(5):
            if symbols[h1.cards[i]] > symbols[h2.cards[i]]: return True
            elif symbols[h1.cards[i]] < symbols[h2.cards[i]]: return False
    elif h1.seq > h2.seq: return True
    else: return False

def CalSeq(cards):
    symCount = {
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'T': 0,
        'J': 0,
        'Q': 0,
        'K': 0,
        'A': 0
    }
    for card in cards:
        symCount[card] += 1

    if 5 in symCount.values(): return sequence.p
    if 4 in symCount.values(): return sequence.k
    if 3 in symCount.values():
        if 2 in symCount.values():
            return sequence.f
        else: return sequence.t
    if 2 in symCount.values():
        if sum(1 for v in symCount.values() if v == 2) >= 2:
            return sequence.p2
        else: return sequence.p1
    return sequence.h


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j].seq.value == arr[j + 1].seq.value:
                swapped = True
                if IsGreaterThan(arr[j], arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif arr[j].seq.value > arr[j + 1].seq.value:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

for i in input:
    d = i.split(' ')
    hands.append(Hand(d[0],int(d[1])))
    #print(i)

# print("Set Seq")
for i in range(len(hands)):
    hand = hands[i]
    hand.seq = CalSeq(hand.cards)
#     print(hand.cards, hand.bid, hand.seq, hand.rank)
# print()
# print(sequence.p1.value)
bubbleSort(hands)


for i in range(len(hands)):
    hand = hands[i]
    hand.rank = i + 1
    answer += (i+1) * hand.bid

for i in range(len(hands)):
    hand = hands[i]
    print(hand.cards, hand.bid, hand.seq, hand.rank)
print("Answer: ", answer)
