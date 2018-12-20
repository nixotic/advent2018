

# DAY 001
# PART 001
input_array = []
with open('Data/input001.txt', 'r') as raw_data:
    for line in raw_data:
        input_array.append(int(line))

freq = 0
for adjust in input_array:
    freq += adjust

print('1-loop freq: %i' % freq)

# PART 002
freq = 0
freqs = []
dup_found = False
while not dup_found:
    for adjust in input_array:
        freq += adjust
        if freq in freqs:
            print('Duplicate freq: %i' % freq)
            dup_found = True
        freqs.append(freq)
