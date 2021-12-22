import day5lib as lib

def part1():
    highestSeatId = 0
    for seat in seats:
        seatId = lib.getSeatId(seat)

        if seatId > highestSeatId:
            highestSeatId = seatId
            print("new highest: " + str(highestSeatId))

def part2():
    list = []
    for seat in seats:
        seatId = lib.getSeatId(seat)
        list.append(seatId)
    
    list.sort()
    
    for i in range(75,865):
        if(i != list[i-75]):
            print("my seat: ", i)
            break


seats = []
with open("F:\\programming\\github\\adventofcode\\python\\day5\\input_01.txt", 'r') as f:
    seats = f.readlines()




#part1()
part2()