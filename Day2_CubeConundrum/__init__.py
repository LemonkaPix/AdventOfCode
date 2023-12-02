from enum import Enum
print("--- Day 2: Cube Conundrum ---")

f = open("input2.txt")
input = f.read().split('\n')
answer = 0
i = 0
for line in input:
    data = line.split(':')
    id = int(data[0].replace("Game ", ""))  #id
    stacksData = data[1].split(';')
    stacks = []
    minR = 0
    minG = 0
    minB = 0
    for stack in stacksData:
        # print(stack)
        items = stack.split(',')

        for item in items:
            itemData = item.split(' ')
            itemData.pop(0)
            print(itemData)
            if(itemData[1] == "red"):
                if(int(itemData[0]) > minR):
                    minR = int(itemData[0])
            elif(itemData[1] == "green"):
                if(int(itemData[0]) > minG):
                    minG = int(itemData[0])
            elif(itemData[1] == "blue"):
                if(int(itemData[0]) > minB):
                    minB = int(itemData[0])


        print()

    print(f"={minR}={minG}={minB}=")
    answer += (minR * minG * minB)

    # print(stacks[0].color)

print("Answer: ", answer)