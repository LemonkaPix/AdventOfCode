import math

print("--- Day 4: Scratchcards ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0

for line in input:
    winNums = line.split(':')
    winNums = winNums[-1].split(" | ")[0].split(' ')
    while ("" in winNums):
        winNums.remove("")

    myNums = line.split(':')
    myNums = myNums[-1].split(" | ")[1].split(' ')
    while ("" in myNums):
        myNums.remove("")

    countOfNums = 0
    for num in myNums:
        if(winNums.__contains__(num)):
            countOfNums += 1

    print(math.floor(math.pow(2, countOfNums - 1)))
    answer += math.floor(math.pow(2, countOfNums - 1))

print("Answer: ", answer)