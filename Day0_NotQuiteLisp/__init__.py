print("--- Day 1: Not Quite Lisp ---")

f = open("input.txt")
input = f.read()
answer = 1
floor = 0
for c in input:
    if(c == '('):
        floor += 1
    else: floor -= 1
    if(floor == -1):
        print("Answer: ", answer)
        break
    answer += 1

