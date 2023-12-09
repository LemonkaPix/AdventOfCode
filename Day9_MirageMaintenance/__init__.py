print("--- Day 9: Mirage Maintenance ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0

def ShowExp(arr):
    for line in arr:
        for item in line:
            print(item, end=" ")
        print()
    print()

for line in input:
    exp = []
    data = [eval(i) for i in line.split()]
    exp.append(data)
    while data.count(0) != len(data):
        tmp = []
        for i in range(len(data)-1):
            tmp.append(data[i+1] - data[i])
        data = tmp
        exp.append(data)

    ShowExp(exp)

    exp[-1].insert(0, 0)
    for i in range(len(exp)-2, -1, -1):
        exp[i].insert(0, exp[i][0] - exp[i+1][0])

    ShowExp(exp)
    answer += exp[0][0]


print("Answer: ", answer)