def carFleet(target, position, speed):
    fleet = []
    for pos, spd in sorted(zip(position, speed), reverse=True):
        time = (target - pos) / spd
        if not fleet or time > fleet[-1]:
            fleet.append(time)
    return len(fleet)


print(
    carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
)  # Expected: 3 (Standard multi-fleet merge)
print(carFleet(10, [3], [3]))  # Expected: 1 (Single car edge case)
print(
    carFleet(100, [0, 2, 4], [4, 2, 1])
)  # Expected: 1 (All cars merge into one big fleet)
print(
    carFleet(10, [6, 8], [3, 2])
)  # Expected: 2 (Car behind catches up right at target, wait: 4/3=1.33 vs 2/2=1.0 -> doesn't catch up)
print(
    carFleet(10, [0, 4, 2], [2, 1, 3])
)  # Expected: 1 (Exact tie at finish line: 5.0, 6.0, 2.67 -> all merge into 6.0)
print(
    carFleet(10, [8, 3, 7, 4, 6, 5], [4, 4, 4, 4, 4, 4])
)  # Expected: 6 (Equal speeds, no car ever catches another)
