print("--- Day 8: Haunted Wasteland ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0
seq = input[0]
input.pop(0)
input.pop(0)

dic = dict()

for line in input:
    data = line.split(" = ")
    key = data[0]
    val = data[1]
    val = val.replace('(',"")
    val = val.replace(')',"")
    tmp = val.split(", ")
    value = (tmp[0],tmp[1])

    dic[key] = value

isEnd = False
code = "AAA"
while not isEnd:

    for chr in seq:
        if(chr == 'L'):
            code = dic[code][0]
        else:
            code = dic[code][1]
        answer += 1
        if code == "ZZZ":
            isEnd = True
            break

print("Answer: ", answer)
