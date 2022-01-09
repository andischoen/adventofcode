import os,re

path = os.path.dirname(os.path.realpath(__file__))

cuboid_specs = []
cuboids = []
with open(path + "\input.txt") as f:
    cuboid_specs = f.readlines()

class Cuboid:
    def init_from_spec(self, cuboid) -> None:
        self.x_low = cuboid["x"][0]
        self.x_high = cuboid["x"][1]
        self.y_low = cuboid["y"][0]
        self.y_high = cuboid["y"][1]
        self.z_low = cuboid["z"][0]
        self.z_high = cuboid["z"][1]

        self.volume = 0
        self._calc_volume()

        self.on_state = cuboid["state"] == "on"
        self.sign = 1

    def __init__(self) -> None:
        self.x_low = 0
        self.x_high = 0
        self.y_low = 0
        self.y_high = 0
        self.z_low = 0
        self.z_high = 0
        self.volume = 0
        self.sign = 0

    def _calc_volume(self):
        x = self.x_high - self.x_low + 1
        y = self.y_high - self.y_low + 1
        z = self.z_high - self.z_low + 1

        self.volume = x*y*z

    def has_overlap(self, other):
        if other.x_high < self.x_low or other.x_low > self.x_high:
            return False
        if other.y_high < self.y_low or other.y_low > self.y_high:
            return False
        if other.z_high < self.z_low or other.z_low > self.z_high:
            return False
        return True

    def get_intersection(self,other):
        intersection = Cuboid()
        intersection.x_low = max([self.x_low,other.x_low])
        intersection.x_high = min([self.x_high,other.x_high])
        intersection.y_low = max([self.y_low,other.y_low])
        intersection.y_high = min([self.y_high,other.y_high])
        intersection.z_low = max([self.z_low,other.z_low])
        intersection.z_high = min([self.z_high,other.z_high])
        intersection.volume = 0
        intersection._calc_volume()
        intersection.sign = -self.sign
        return intersection


def part1_startup_sequence(cuboids):
    reactor = dict()
    for cuboid in cuboids:
        state = True if cuboid["state"] == 'on' else False
    
        if cuboid["x"][0] > 50 or cuboid["x"][1] < -50 or cuboid["y"][0] > 50 or cuboid["y"][1] < -50 or cuboid["z"][0] > 50 or cuboid["z"][1] < -50:
            continue
    
        for x in range(cuboid["x"][0],cuboid["x"][1]+1):
            for y in range(cuboid["y"][0],cuboid["y"][1]+1):
                for z in range(cuboid["z"][0],cuboid["z"][1]+1):
                    reactor[(x,y,z)] = state
    return reactor

def get_on_cubes(cuboids):
    count = 0

    cuboid_sequnce = []
    for cuboid in cuboids:
        c = Cuboid()
        c.init_from_spec(cuboid)
        
        intersections = []
        if c.on_state: intersections.append(c)
        for sc in cuboid_sequnce:
            if sc.has_overlap(c):
                intersections += [sc.get_intersection(c)]
        
        cuboid_sequnce += intersections
    sc:Cuboid
    for sc in cuboid_sequnce:
        count += sc.sign*sc.volume
    return count
    
    
for cuboid_spec in cuboid_specs:
    match = re.search("(\w+) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)",cuboid_spec.strip())
    cuboids.append({"state":match.group(1),"x":[int(match.group(2)),int(match.group(3))], "y":[int(match.group(4)),int(match.group(5))], "z":[int(match.group(6)),int(match.group(7))]})



# reactor = part1_startup_sequence(cuboids)

# print("Part1: number of on-cubes = " + str(len([c for c in reactor if reactor[c]])))

#part2

count = get_on_cubes(cuboids)

print("Part 2: number of on-cubes = " + str(count))