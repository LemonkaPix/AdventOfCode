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

    if(key[-1] == 'A'): codes.append(key)

    dic[key] = value

isEnd = False

while not isEnd:

    for chr in seq:
        for i in range(len(codes)):
            code = codes[i]
            if(chr == 'L'):
                codes[i] = dic[code][0]
            else:
                codes[i] = dic[code][1]
        print(codes)

        answer += 1

        isEnd = True
        for i in codes:
            if i[-1] != 'Z':
                isEnd = False
                break
        if isEnd: break

print("Answer: ", answer)
