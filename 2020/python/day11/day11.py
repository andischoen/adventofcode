import day11lib as lib


seats = []

with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day11\\input_01.txt", 'r') as f:
    seats = f.readlines()

for i in range(len(seats)):
    seats[i] = list(seats[i].strip())

lib.setSeats(seats)

# part 1
switch = lib.switchSeats()
count = 0
while switch:
    switch = lib.switchSeats()
    count += 1
    print("switching # " + str(count))

print("Occupied seat # " + str(lib.getOccupiedSeats()))

with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day11\\input_01.txt", 'r') as f:
    seats = f.readlines()

for i in range(len(seats)):
    seats[i] = list(seats[i].strip())

lib.setSeats(seats)

# part 2
switch = lib.switchSeats2()
count = 0
while switch:
    switch = lib.switchSeats2()
    count += 1
    print("switching # " + str(count))

print("Occupied seat # " + str(lib.getOccupiedSeats()))