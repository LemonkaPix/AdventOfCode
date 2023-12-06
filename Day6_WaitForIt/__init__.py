print("--- Day 6: Wait For It ---")

f = open("input.txt")
input = f.read().split('\n')
answer = 0

tmp = input[0].split(':')
tmp.pop(0)
time = int(tmp[0].replace(" ",""))

tmp = input[1].split(':')
tmp.pop(0)
dist = int(tmp[0].replace(" ",""))

print(time)
print(dist)

for t in range(int((time))):
    if(t * (time-t) > dist): answer += 1

# for i in range(iteration):
#     for time in range(times[i]+1):
#         if(time * (times[i]-time) > dists[i]): answer += 1

print("Answer: ", answer)