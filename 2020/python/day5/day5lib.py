def getBinarySeat (seat, lowerRange, upperRange):
    lower = lowerRange
    upper = upperRange

    for i in range(len(seat)):
        half = ((upper - lower + 1) / 2)
        upperHalf = lower + half
        if seat[i] == 'F' or seat[i] == 'L':
            upper = upperHalf-1
        else:
            lower = upperHalf
    
    return upper

def getSeatId(seat):
    row = getBinarySeat(seat[0:7], 0, 127)
    col = getBinarySeat(seat[7:10], 0, 7)

    seatId = (row * 8) + col
    return seatId