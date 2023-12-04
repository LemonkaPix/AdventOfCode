import math

print("--- Day 4: Scratchcards ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0
cards = [1] * len(input)
currCard = 0
for line in input:
    currCard += 1
    winNums = line.split(':')
    winNums = winNums[-1].split(" | ")[0].split(' ')
    while ("" in winNums):
        winNums.remove("")

    myNums = line.split(':')
    myNums = myNums[-1].split(" | ")[1].split(' ')
    while ("" in myNums):
        myNums.remove("")

    for count in range(cards[currCard - 1]):
        countOfNums = 0
        for num in myNums:
            if(winNums.__contains__(num)):
                countOfNums += 1

        for i in range(countOfNums):
            cards[currCard + i] += 1
    print(currCard)

for card in cards:
    answer += card

print(cards)
print("Answer: ", answer)