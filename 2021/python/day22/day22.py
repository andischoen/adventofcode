import os,re

path = os.path.dirname(os.path.realpath(__file__))

cuboid_specs = []
cuboids = []
with open(path + "\input.txt") as f:
    cuboid_specs = f.readlines()

for cuboid_spec in cuboid_specs:
    match = re.search("(\w+) x=(\-?\d+)..(\-?\d+),y=(\-?\d+)..(\-?\d+),z=(\-?\d+)..(\-?\d+)",cuboid_spec.strip())
    cuboids.append({"state":match.group(1),"x":[int(match.group(2)),int(match.group(3))], "y":[int(match.group(4)),int(match.group(5))], "z":[int(match.group(6)),int(match.group(7))]})

reactor = dict()
for cuboid in cuboids:
    state = True if cuboid["state"] == 'on' else False
    
    if cuboid["x"][0] > 50 or cuboid["x"][1] < -50 or cuboid["y"][0] > 50 or cuboid["y"][1] < -50 or cuboid["z"][0] > 50 or cuboid["z"][1] < -50:
        continue
    
    for x in range(cuboid["x"][0],cuboid["x"][1]+1):
        for y in range(cuboid["y"][0],cuboid["y"][1]+1):
            for z in range(cuboid["z"][0],cuboid["z"][1]+1):
                reactor[(x,y,z)] = state


print("Part1: number of on-cubes = " + str(len([c for c in reactor if reactor[c]])))