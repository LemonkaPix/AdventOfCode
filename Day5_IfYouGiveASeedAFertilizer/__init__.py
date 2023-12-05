print("--- Day 5: If You Give A Seed A Fertilizer ---")

f = open("input.txt")
input = f.read().split("\n\n")
answer = 0

tmp = input[0].split(": ")[-1].split(' ')
seeds = []
for i in range(0, len(tmp), 2):
    seeds.append([int(tmp[i]), int(tmp[i+1])])

# for i in tmp:
#     seeds.append(int(i))
print("seeds: " + str(seeds))

tables = []
for i in range(1, len(input)):
    item = input[i]
    item = item.split('\n')
    item.pop(0)
    record = []
    for j in item:
        nums = j.split(' ')
        newarr = []
        for k in nums:
            newarr.append(int(k))
        record.append(newarr)
    tables.append(record)

for i in tables:
    for j in i:
        print(j)
    print()

def convert(num, table):
    add = -1
    for rng in tables[table]:
        if(num >= rng[1] and num < rng[1] + rng[2]):
            add = num - rng[1] + rng[0]
    if(add == -1): return num
    else: return add

output = []
v = 1
for seedPair in seeds:
    for seed in range(seedPair[0],seedPair[0]+seedPair[1]):
        for tableIndex in range(len(tables)):
            seed = convert(seed, tableIndex)
        output.append(seed)
        print(v)
        v += 1

answer = min(output)
print("Answer: ", answer)