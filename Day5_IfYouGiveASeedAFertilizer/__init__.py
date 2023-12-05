print("--- Day 5: If You Give A Seed A Fertilizer ---")

f = open("input.txt")
input = f.read().split("\n\n")
ot = open("output.txt", 'w')
fstr = ""

f.close()
answer = 0

tmp = input[0].split(": ")[-1].split(' ')
seeds = []
for i in range(0, len(tmp), 2):
    seeds.append([int(tmp[i]), int(tmp[i+1])])

max = 0
min = 100000000000
for i in tmp:
    seeds.append(int(i))

for i in range(0, len(seeds), 2):
    val = seeds[1]
    if(val[0] + val[1] > max): max = val[0] + val[1]
    if(val[0] < min): min = val[0]
print(max)
print(min)
iterations = max - min
print(iterations)

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

# for i in tables:
#     for j in i:
#         print(j)
#     print()

def convert(num, table):
    add = -1
    for rng in tables[table]:
        if(num >= rng[1] and num < rng[1] + rng[2]):
            add = num - rng[1] + rng[0]
    if(add == -1): return num
    else: return add

output = []
v = 0
seedI = 0

# for seedPair in seeds:
#     answer += seedPair[1]
for seedPair in seeds:
    seedC = 0
    seedI += 1

    fstr = ""
    for seed in range(seedPair[0],seedPair[0]+seedPair[1]):
        v += 1
        seedC += 1
        for tableIndex in range(len(tables)):
            seed = convert(seed, tableIndex)
        output.append(seed)
        if(v % 100000 == 0): print(f"seed: {seedI}/{len(seeds)}, seed%: {seedC / seedPair[1] * 100}% \n{v}")
        fstr += str(seed) + "\n"
    fstr += "\n"
    ot.write(str(min(output)) + "\n")
answer = min(output)

print("Answer: ", answer)