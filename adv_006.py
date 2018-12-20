from statistics import mean
from math import sin, cos, atan, pi


def add_tuple(t1, t2):
    a = t1[0] + t2[0]
    b = t1[1] + t2[1]
    return (a, b)


def sub_tuple(t1, t2):
    a = t1[0] - t2[0]
    b = t1[1] - t2[1]
    return (a, b)


def taxi_distance(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))


def value_in_discontinous(check, range_list):  # looks for values in a list of discrete values and range pairs
    result = False
    for val in range_list:
        if type(val) is list:
            if (check <= max(val)) and (check >= min(val)):
                result = True
        elif val == check:
            result = True
    return result


def add_to_mask(range_list, rad, short_angle):  #
    prev_rad = rad - 1
    if prev_rad is not 0:
        prev_min_angle = (1/(prev_rad*4))
        bracket_high = short_angle + prev_min_angle
        bracket_low = short_angle - prev_min_angle
        if bracket_low < 0:
            bracket_low += 1
        if bracket_high >= 1:
            bracket_high -= 1

        mask_added = False
        # Simple case: we've got a value between two previous values so block them out as a range
        if (bracket_high in range_list[2]) and (bracket_low in range_list[2]):
            range_list[2].remove(bracket_low)
            range_list[2].remove(bracket_high)
            range_list[1].append((bracket_low, bracket_high))
            mask_added = True
        else:  # we don't have matching discrete angles
            for range_pair in range_list[1]:
                if range_pair[0] < range_pair[1]:  # need to check if the range includes zero
                    # Check if the lower bracket is captured within an existing masked range
                    if (range_pair[0] <= bracket_low <= range_pair[1]) and (range_pair[1] < short_angle):
                        range_list[1].remove(range_pair)
                        range_list[1].append((range_pair[0], short_angle))  # expand this range pair upwards
                        mask_added = True
                    # Check if the upper bracket is captured within an existing masked range
                    elif (range_pair[0] <= bracket_high <= range_pair[1]) and (range_pair[0] > short_angle):
                        range_list[1].remove(range_pair)
                        range_list[1].append((short_angle, range_pair[1]))  # expand this range pair downwards
                        mask_added = True
                else:  # range pair includes zero (eg from the range from 0.75 to 0.25)
                    # Check if the lower bracket is captured within an existing masked range
                    if (bracket_low >= range_pair[0]) \
                            and 0 <= bracket_low <= (range_pair[1])\
                            and (range_pair[1] < short_angle):
                        range_list[1].remove(range_pair)
                        range_list[1].append((range_pair[0], short_angle))  # expand this range pair upwards
                        mask_added = True

            if not mask_added:
                range_list[2].append(short_angle)







    else:  # this is one of the first blocked angles - a range can't be formed yet
        range_list[2].append(short_angle)
        return range_list







raw = []
with open('Data/input006.txt', 'r') as file:
    for line in file:
        raw.append(line)


coords = []
for pair in raw:
    x, y = pair.split(',')
    coords.append((int(x), int(y)))


xmax = max(coords, key=lambda x: x[0])[0]
ymax = max(coords, key=lambda x: x[1])[1]
xmin = min(coords, key=lambda x: x[0])[0]
ymin = min(coords, key=lambda x: x[1])[1]

buf = 50
grid_xmax = xmax - xmin + buf
grid_ymax = ymax - ymin + buf

points_size = {}
norm_points = []
for pair in coords:
    normed_point = sub_tuple(pair, ((xmin + buf), (ymin + buf)))
    norm_points.append(normed_point)
    points_size[normed_point] = [1, [False, [],[]]]  # Assuming no duplicates - each space at contains its own origin
    # points_size[normed_point][0] is the number of squares/coordinates associated with the region
    # points_size[normed_point][1][0] indicates if the region is complete and bounded
    # points_size[normed_point][1][1] is a list of range tuples that describe bound angles
    # points_size[normed_point][1][1] is a list of discrete angles that have been bound





grid = [[None]*grid_xmax for i in range(grid_ymax)]

radius = 0

for point in points_size:
    # noinspection PyTypeChecker
    grid[point[0]][point[1]] = [point, 0]
    radius += 1
    d = radius*4
    for r in range(d):  # We iterate over points on the Manhatten circle
        angle = 2*pi*(r/d)
        if angle not in points_size[point][1]:
            pass
        x_delta = round(cos(angle)*radius)
        y_delta = round(sin(angle)*radius)
        check_point = add_tuple(point, (x_delta, y_delta))
        # noinspection PyTypeChecker
        if grid[check_point[0]][check_point[1]] is None:
            grid[check_point[0]][check_point[1]] = [point, radius]
            points_size[point][0] += 1
        elif grid[check_point[0]][check_point[1]][1] > radius:  # probably shouldn't happen...
            grid[check_point[0]][check_point[1]] = [point, radius]
            points_size[point][0] += 1
        elif grid[check_point[0]][check_point[1]][1] == radius:  # we've just bumped into another region
            # noinspection PyTypeChecker
            grid[check_point[0]][check_point[1]] = ['#', 0]
            points_size[point][1].append(r/d)
        elif grid[check_point[0]][check_point[1]][1] < radius:  # we've just crossed into another region
            points_size[point][1] = add_to_mask(points_size[point][1], radius, r)
            pass  # need to add this angle to list of masked angles





        # print('(%f, %f)' % (xd, yd))
        #p1 = x*1, y*0
        #p2 = x*0, y*1
        #p3 = x*-1, y*0
        #p4 = x*0, y*-1



# results = {}
# for v in range(len(coords)):
#     for w in range(len(coords)):
#         if v != w:
#             dist = taxi_distance(coords[v], coords[w])
#             if coords[v] not in results:
#                 results[coords[v]] = [dist]
#             else:
#                 results[coords[v]].append(dist)
#
# for key in results:
#     results[key] = mean(results[key])


# for key in results:
#     if (xmax == key[0]) or (xmin == key[0]):
#         results[key] = 0.0
#     elif (ymax == key[1]) or (ymin == key[1]):
#         results[key] = 0.0
#
# print(max(results.items(),key=lambda x: x[1]))


# for x in range(grid_size):
#     if x % 100 == 0:
#         print(x)
#     for y in range(grid_size):
#         dist_list = []
#         for coord in coords:
#             z = taxi_distance((x, y), coord)
#             if (x, y) == coord:
#                 grid[x][y] = 'X'
#             else:
#                 dist_list.append({coord: z})
#         dist_list.sort(key=lambda x: max(x.values()))
#         # dist_list.reverse()
#         if list(dist_list[0].values())[0] == list(dist_list[1].values())[0]:
#             grid[x][y] = '.'
#         elif results[list(dist_list[0].keys())[0]] == 0.0:
#             grid[x][y] = '.'
#         else:
#             grid[x][y] = list(dist_list[0].keys())[0]
#             coords_size[list(dist_list[0].keys())[0]] += 1
#
# print(max(coords_size.items(), key=lambda x: x[1]))
# print(coords_size[(94,355)])


# print(results)
#A#Bxx
####Cccccc
#ddDxxxx
#eeEeee
#eeeee
