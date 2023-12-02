from enum import Enum
print("--- Day 2: Cube Conundrum ---")

class Color(Enum):
    red = 1
    green = 2
    blue = 3

class Stack:
    def __init__(self, count, color):
        self.count = count
        self.color = color

class Data:
    def __init__(self, id, stacks):
        self.id = id
        self.stacks = stacks

f = open("input.txt")
input = f.read().split('\n')
answer = 0
i = 0
for line in input:
    data = line.split(':')
    id = int(data[0].replace("Game ", ""))  #id
    stacksData = data[1].split(';')
    stacks = []
    possible = True
    for stack in stacksData:
        # print(stack)
        items = stack.split(',')

        for item in items:
            itemData = item.split(' ')
            itemData.pop(0)
            print(itemData)
            if(int(itemData[0]) > 12 and itemData[1] == "red"):
                possible = False
            elif(int(itemData[0]) > 13 and itemData[1] == "green"):
                possible = False
            elif(int(itemData[0]) > 14 and itemData[1] == "blue"):
                possible = False

        print()

    print(f"========{possible}=========")
    if(possible): answer += id;

    # print(stacks[0].color)

print("Answer: ", answer)