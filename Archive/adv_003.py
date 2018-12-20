# PART 001
data_arr = []
with open('Data/input003.txt', 'r') as raw_input:
    for line in raw_input:
        data_arr.append(line)

processed = []
for entry in data_arr:
    idx = entry.index(' ')
    leftx = entry.index('@') + 2
    topx = entry.index(',') + 1
    wx = entry.index(' ', topx) + 1
    hx = entry.index('x') + 1
    id = entry[:idx]
    left = entry[leftx:topx-1]
    top = entry[topx:wx-2]
    width = entry[wx:hx-1]
    height = entry[hx:]
    processed.append({'id': id,
                      'left': int(left),
                      'top': int(top),
                      'width': int(width),
                      'height': int(height)})
cloth_size = 1000
cloth = [[None]*cloth_size for i in range(cloth_size)]


for p in processed:
    x1 = p['left']
    x2 = p['left'] + p['width']
    y1 = p['top']
    y2 = p['top'] + p['height']
    xrange = range(x1, x2)
    yrange = range(y1, y2)

    for x in xrange:
        for y in yrange:
            if cloth[x][y] is not None:
                cloth[x][y].append(p['id'])
            else:
                cloth[x][y] = [p['id']]

area = 0
ids = []
for p in processed:
    ids.append(p['id'])

for i in range(cloth_size):
    for j in range(cloth_size):
        if cloth[i][j] is not None:
            if len(cloth[i][j]) > 1:
                for id in cloth[i][j]:
                    if id in ids:
                        ids.remove(id)
                area += 1

print(area)
# PART002
print(ids)


