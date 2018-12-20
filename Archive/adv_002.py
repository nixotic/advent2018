
# DAY 002
# Part 001

ids = []
with open('Data/input002.txt', 'r') as raw_input:
    for line in raw_input:
        ids.append(line.rstrip('\n'))

double = 0
triple = 0

for id in ids:
    d = False
    t = False
    for char in id:
        c = id.count(char)
        if c == 2:
            d = True
        if c == 3:
            t = True
    if d:
        double += 1
    if t:
        triple += 1

print(double*triple)

# PART 002
candidate_pairs = []
for id in ids:
    for i in range(len(id)):
        for id2 in ids:
            if id != id2:
                if id[i] != id2[i]:
                    x1 = id[:i]
                    x2 = id[i+1:]
                    y1 = id2[:i]
                    y2 = id2[i+1:]
                    if x1 == y1 :
                        if x2 == y2:
                            print('%s%s' % (x1, x2))

