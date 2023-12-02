print("--- Day 1: Trebuchet?! ---")

f = open("Input2.txt")
# f = open("input.txt")
input = f.read().split('\n')
secondInput = ""
#--- Part Two ---
txtDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
appearanceI = [0, 0, 0, 0, 0, 0, 0, 0, 0]
k = 0
for line in input:                      #wiersz lini
    secondInput = line
    for j in range(len(line)):

        for i in range(len(txtDigits)):
            index = secondInput.find(txtDigits[i])
            if(index == -1):
                appearanceI[i] = 100
            else: appearanceI[i] = index
        # print(secondInput)
        # print(appearanceI)
        lowestI = appearanceI.index(min(appearanceI))
        lowest = txtDigits[appearanceI.index(min(appearanceI))]
        # print(lowest)
        secondInput = secondInput.replace(lowest, str(lowestI + 1))
        # print(secondInput.replace(lowest, str(lowestI + 1)) + "\n")
    print(secondInput)
    input[k] = secondInput
    k+=1
#     input = secondInput.split("\n")
#     secondInput = ""
# for line in input:
#     line = line[::-1]
#
#     for i in range(len(txtDigits)):
#         index = line.find(txtDigits[::-1][i])
#         if(index == -1):
#             appearanceI[i] = 100
#         else: appearanceI[i] = index
#     print(line)
#     print(appearanceI)
#     lowestI = appearanceI.index(max(appearanceI))
#     lowest = txtDigits[::-1][appearanceI.index(max(appearanceI))]
#     print(lowest[::-1])
#     secondInput += line.replace(lowest[::-1], str(lowestI + 1)) + "\n"
#     print(line.replace(lowest[::-1], str(9 - lowestI)) + "\n")
#     print()

#end

answer = 0

print()

for line in input:
    for chr in line:
        if(chr.isdigit()):
            d1 = chr
            break

    for i in range(len(line), 0, -1):
        index = i - 1
        if(line[index].isdigit()):
            d2 = line[index]
            break

    print(d1 + d2)
    output = d1 + d2
    answer += int(output)
print("Answer: ", answer)