import math

# target area: x=20..30, y=-10..-5
# target area: x=257..286, y=-101..-57

t_min_x = 257
t_max_x = 286
t_min_y = -101
t_max_y= -57

reduction = dict()

def init_reduction_dict():
    sum = 0
    for i in range(1,5001):
        reduction[i] = sum
        sum += i

def hit_check(vx,vy):
    hit = False
    
    min_steps = 1
    if vy > 0:
        min_steps = (vy*2)+1

    for s in range(min_steps,1000):
        y = vy*s-reduction[s]
        x = 0
        if vx > s:
            x = vx*s-reduction[s]
        else:
            x = int(vx*(vx+1)/2)
        
        if x >= t_min_x and x <= t_max_x and y >= t_min_y and y <= t_max_y:
            hit = True
            break
            
        if x > t_max_x or y < t_min_y:
            break

    return hit

init_reduction_dict()

vy_max = abs(t_min_y)-1
max_y = (vy_max*(vy_max + 1))/2
print("Part1: maximum y = " + str(max_y) + 
      " - we only need to think about y verlocity - the probe always comes back to y=0 and is than at the negative starting speed," + 
      " so from 0 down to the furtherst point is automatically equal the starting speed +1. From there it's just the sum all numbers from 1 to starting speed")


# sum = n*(n+1)/2 <=> 0 = n^2+n-2*sum <=> -0,5 +- sqrt(0,25+2*sum)
vx_max = t_max_x
vx_min = math.ceil(-0.5+math.sqrt(0.25+2*t_min_x))
vy_min = t_min_y

count = 0
for vx in range(vx_min, vx_max+1):
    for vy in range(vy_min, vy_max+1):
        if hit_check(vx,vy):
            count += 1


print("Part2: number of possible velocities = " + str(count))