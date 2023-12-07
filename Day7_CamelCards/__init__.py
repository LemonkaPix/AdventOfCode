from enum import Enum

print("--- Day 7: Camel Cards ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0
hands = []

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
    def __init__(self, card, bid):
        self.card = card
        self.bid = bid
        self.rank = 0
        self.seq = 0

def IsGreaterThan(h1, h2)
    if h1 == h2
    #SKOŃCZYŁEM TUTAJ

for i in input:
    d = i.split(' ')
    hands.append(Hand(d[0],int(d[1])))
    #print(i)

for i in hands:
    print(i.card, i.bid)



    

print("Answer: ", answer)
