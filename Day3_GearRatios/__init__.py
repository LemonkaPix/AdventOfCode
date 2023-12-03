print("--- Day 3: Gear Ratios ---")

class Bit:
    def __init__(self, num, gear):
        self.num = num
        self.gear = gear

f = open("input.txt")
input = f.read().split('\n')
answer = 0
# map = [[False] * len(input[0])] * len(input)
map = []

for line in input:
    tempArr = []
    for i in line:
        tempArr.append(0)
    map.append(tempArr)

currentNum = ""
currentGear = 0
gearCount = 0
isPart = False
gearIndex = 1
gearNeigh = []
nums = []

for y in range(len(input)):
    for x in range(len(input[y])):
        chr = input[y][x]
        # mapowanie
        if(chr == '*'):
            for vy in range(-1,2):
                for vx in range(-1,2):
                    ny = y + vy
                    nx = x + vx
                    if (ny >= 0 and ny < len(input) and nx >= 0 and nx < len(input[y])):
                        map[ny][nx] = gearIndex
            gearIndex += 1
            gearCount += 1
            gearNeigh.append(0)

for y in range(len(input)):
    for x in range(len(input[y])):
        chr = input[y][x]
        if(chr.isdigit()):
            currentNum += chr
            if(map[y][x] > 0):
                isPart = True
                currentGear = map[y][x]
        else:
            if(isPart == True):
                # answer += int(currentNum)
                nums.append(Bit(int(currentNum), currentGear))
            currentNum = ""
            currentGear = 0
            isPart = False

if (isPart == True):
    # answer += int(currentNum)
    nums.append(Bit(int(currentNum), currentGear))
currentNum = ""
isPart = False

print()

for i in nums:
    print(str(i.num)+ " " + str(i.gear))
print(gearCount)

for i in range(gearCount):
    countOfNums = 0
    rightNums = []
    for num in nums:
        if (num.gear == i+1):
            countOfNums += 1
            rightNums.append(num.num)
    if(countOfNums >= 2):
        answer += rightNums[0] * rightNums[1]
    else:
        rightNums = []

print()
for line in map:
    for i in line:
        print(int(i),end=" ")
    print()

print("Answer: ", answer)
