import re
print("--- Day 1: Trebuchet?! ---")


f = open("testInput2.txt")
# f = open("input.txt")
input = f.read().split('\n')
secondInput = ""
#--- Part Two ---
# txtDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# appearanceI = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# k = 0
# for line in input:                      #wiersz lini
#     secondInput = line
#     for j in range(len(line)):
#
#         for i in range(len(txtDigits)):
#             index = secondInput.find(txtDigits[i])
#             if(index == -1):
#                 appearanceI[i] = 100
#             else: appearanceI[i] = index
#         # print(secondInput)
#         # print(appearanceI)
#         lowestI = appearanceI.index(min(appearanceI))
#         lowest = txtDigits[appearanceI.index(min(appearanceI))]
#         # print(lowest)
#         secondInput = secondInput.replace(lowest, str(lowestI + 1))
#         # print(secondInput.replace(lowest, str(lowestI + 1)) + "\n")
#     print(secondInput)
#     input[k] = secondInput
#     k+=1


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

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
wordsd = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def replace_words_with_numbers(text):
    indexes = []
    for word in words:
        indexes += re.finditer(word, text)
    return indexes

# matches = replace_words_with_numbers("eightwo3")
# print(matches[0])

newInput = []
for line in input:
    tmpString = ""
    matches = replace_words_with_numbers(line)
    min = 1000
    minI = 1000
    max = 0
    maxI = 0

    # tmpString = str(matches[0].re.pattern)
    # tmpString += str(matches[-1].re.pattern)

    for j in range(len(matches)):
        index = int(matches[j].regs[0][0])
        if(index < min):
            min = index
            minI = j
        if(index > max):
            max = index
            maxI = j

    print()
    tmpString += str(matches[minI].re.pattern)
    tmpString += str(matches[maxI].re.pattern)


    for i in range(len(wordsd)):
        w = wordsd[i]
        if(re.search(w, tmpString)):
            tmpString = tmpString.replace(w, str(i+1))

    newInput.append(tmpString)

for i in newInput:
    answer += int(i)


# for line in input:
#     for chr in line:
#         if(chr.isdigit()):
#             d1 = chr
#             break
#
#     for i in range(len(line), 0, -1):
#         index = i - 1
#         if(line[index].isdigit()):
#             d2 = line[index]
#             break
#
#     print(d1 + d2)
#     output = d1 + d2
print(answer)
