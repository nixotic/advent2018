
events_raw = []
with open('Data/input004.txt', 'r') as file:
    for line in file:
        events_raw.append(line)


guards = {}
events = []
for raw in events_raw:
    year = int(raw[1:5])
    month = int(raw[6:8])
    day = int(raw[9:11])
    hour = int(raw[12:14])
    minute = int(raw[15:17])
    event_type = raw[19:20]

    if event_type not in ['w', 'f', 'G']:
        raise ValueError('Unexpected data')

    if event_type == 'G':
        guard_id = raw[25:raw.index(' ', 25)]
    else:
        guard_id = None

    description = [year, month, day, hour, minute, event_type, guard_id]
    events.append(description)
        # print(year)
        # print(month)
        # print(day)
        # print(hour)
        # print(minute)
        # print(event_type)
        # print(guard_id)
        # quit()

    if event_type == 'G':
        if guard_id not in guards:
            guards[guard_id] = [0]*60

events.sort(key=lambda x: x[0]*365*31*24*60 + x[1]*31*24*60 + x[2]*24*60 + x[3]*60 + x[4])

current_guard = ''
current_sleep_m = 0
current_wake_m = 0
for event in events:
    if event[5] == 'G':
        current_guard = event[6]
    elif event[5] == 'f':
        current_sleep_m = event[4]
    elif event[5] == 'w':
        current_wake_m = event[4]
        for i in range(current_sleep_m, current_wake_m):
            guards[current_guard][i] += 1

guard_pick = max(guards.items(), key=lambda x: max(x[1]))

print(guard_pick)
print(guard_pick[1].index(max(guard_pick[1])))
print(45*2663)
print(25*509)
