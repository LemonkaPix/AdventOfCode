import math

print("--- Day 8: Haunted Wasteland ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0
seq = input[0]
input.pop(0)
input.pop(0)

dic = dict()

codes = []

for line in input:
    data = line.split(" = ")
    key = data[0]
    val = data[1]
    val = val.replace('(',"")
    val = val.replace(')',"")
    tmp = val.split(", ")
    value = (tmp[0],tmp[1])
    if (key[-1] == 'A'): codes.append(key)
    dic[key] = value

def CalLenghth(_code):
    isEnd = False
    startCode = _code
    code = startCode
    output = 0
    while not isEnd:

        for chr in seq:
            if code[-1] == "Z" and dic[code][1 if chr == 'L' else 0]:
                isEnd = True
                break
            if(chr == 'L'):
                code = dic[code][0]
            else:
                code = dic[code][1]
            output += 1
    return output

clm = []
for i in codes:
    clm.append(CalLenghth(i))

answer = math.lcm(*clm)

print("Answer: ", answer)
