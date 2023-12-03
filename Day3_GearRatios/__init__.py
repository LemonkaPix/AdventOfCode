print("--- Day 3: Gear Ratios ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0
# map = [[False] * len(input[0])] * len(input)
map = []

for line in input:
    tempArr = []
    for i in line:
        tempArr.append(False)
    map.append(tempArr)

currentNum = ""
isPart = False

for y in range(len(input)):
    for x in range(len(input[y])):
        chr = input[y][x]
        # mapowanie
        if(not chr.isdigit() and chr != '.'):
            for vy in range(-1,2):
                for vx in range(-1,2):
                    ny = y + vy
                    nx = x + vx
                    if(ny >=0 and ny <= len(input) and nx >=0 and ny <= len(input[y])):
                        # print(str(ny) + " " + str(nx))
                        map[ny][nx] = True
        #

for y in range(len(input)):
    for x in range(len(input[y])):
        chr = input[y][x]
        if(chr.isdigit()):
            currentNum += chr
            if(map[y][x] == True): isPart = True;
        else:
            if(isPart == True):
                print(currentNum)
                answer += int(currentNum)
            currentNum = ""
            isPart = False





# for line in map:
#     for i in line:
#         print(int(i),end=" ")
#     print()

print("Answer: ", answer)
