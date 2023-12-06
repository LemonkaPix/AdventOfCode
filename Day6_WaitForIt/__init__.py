print("--- Day 6: Wait For It ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 1

tmp = input[0].split()
tmp.pop(0)
times = [int(x) for x in tmp]

tmp = input[1].split()
tmp.pop(0)
dists = [int(x) for x in tmp]

print(times)
print(dists)

iteration = len(times)

for i in range(iteration):
    possib = 0
    for time in range(times[i]+1):
        if(time * (times[i]-time) > dists[i]): possib += 1
    answer = answer * possib

print("Answer: ", answer)