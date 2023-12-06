import sys
import re
from collections import defaultdict

print("--- Day 5: If You Give A Seed A Fertilizer ---")
f = open("input.txt")
input = f.read().split("\n\n")
tmp = input[0].split(": ")[-1].split(' ')
seeds = []

for i in range(0, len(tmp), 2):
    seeds.append([int(tmp[i]), int(tmp[i+1])])
# for i in tmp:
#     seeds.append(int(i))
# print("seeds: " + str(seeds))
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
    record.sort(key=lambda x: x[1])
    tables.append(record)



# for i in tables:
#     for j in i:
#         print(j)
#     print()

def convert(rng, table):
    output = []
    (min, max) = rng
    isInRange = True
    for R in tables[table]:
        minR = R[1]
        maxR = R[1] + R[2]
        outR = R[0]
        if(min >= minR and max <= maxR):
            return [(min - minR + outR, max - minR + outR)]
        elif(min >= minR and min < maxR and max > maxR):
            output.append((min - minR + outR, maxR - minR + outR-1))
            for i in convert((maxR, max), table):
                output.append(i)
            isInRange = True
        elif(min >= maxR or max < minR):
            isInRange = False
    if isInRange == False:
        output.append((min, max))
    return output

def apply_range(R):
    A = []
    for table in tables:
        dest = table[0]
        src = table[1]
        sz = table[2]
        src_end = src+sz
        NR = []
        while R:
            # [st                                     ed)
            #          [src       src_end]
            # [BEFORE ][INTER            ][AFTER        )
            (st,ed) = R.pop()
            # (src,sz) might cut (st,ed)
            before = (st,min(ed,src))
            inter = (max(st, src), min(src_end, ed))
            after = (max(src_end, st), ed)
            if before[1]>before[0]:
              NR.append(before)
            if inter[1]>inter[0]:
              A.append((inter[0]-src+dest, inter[1]-src+dest))
            if after[1]>after[0]:
              NR.append(after)
        R = NR
    return A+R


output = []
# v = 1
# for seedPair in seeds:
#     for seed in range(seedPair[0],seedPair[0]+seedPair[1]):
#         for tableIndex in range(len(tables)):
#             seed = convert(seed, tableIndex)
#         output.append(seed)
#         # print(v)
#         v += 1

# for i in range(len(tables)-1,-1,-1):
#     table = tables[i]
#     minR = []
#     minimal = 1000000000000
#     for R in table:
#         if(R[0] < minimal): minR = R
#     print()

# answer = min(output)
for seed in seeds:
    seedR = (seed[0],seed[0]+seed[1])

    stf = []
    ftw = []
    wtl = []
    ltt = []
    tth = []
    htl = []

    sts = [x for x in convert(seedR, 0)]
    for i in sts: stf = [x for x in convert(i, 1)]
    for i in stf: ftw = [x for x in convert(i,2)]
    for i in ftw: wtl = [x for x in convert(i,3)]
    for i in wtl: ltt = [x for x in convert(i,4)]
    for i in ltt: tth = [x for x in convert(i,5)]
    for i in tth: htl = [x for x in convert(i,6)]

    for j in htl:
        output.append(j)
    # print(htl)
print(apply_range([(2361566863, 262106125)]))
answer = min(output, key = lambda x: x[0])




print("Answer: ", answer)